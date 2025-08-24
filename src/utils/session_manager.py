#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerenciador de Sessões - Médico de Bolso
Gerencia sessões de usuários e histórico de conversas
"""

import time
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from threading import Lock
from src.config.settings import SESSION_TIMEOUT
from src.utils.logger import medical_logger

logger = logging.getLogger(__name__)

@dataclass
class UserSession:
    """Representa uma sessão de usuário"""
    user_id: int
    user_name: str = ""
    start_time: float = field(default_factory=time.time)
    last_activity: float = field(default_factory=time.time)
    messages: List[Dict[str, Any]] = field(default_factory=list)
    medical_context: Dict[str, Any] = field(default_factory=dict)
    is_active: bool = True

class SessionManager:
    """Gerenciador de sessões de usuários"""
    
    def __init__(self):
        """Inicializa o gerenciador de sessões"""
        self.sessions: Dict[int, UserSession] = {}
        self.lock = Lock()
        logger.info("Gerenciador de sessões inicializado")
    
    def create_session(self, user_id: int, user_name: str = "") -> UserSession:
        """Cria uma nova sessão para o usuário"""
        with self.lock:
            # Finalizar sessão anterior se existir
            if user_id in self.sessions:
                self._end_session(user_id)
            
            # Criar nova sessão
            session = UserSession(user_id=user_id, user_name=user_name)
            self.sessions[user_id] = session
            
            # Log da criação da sessão
            medical_logger.log_session_start(user_id, user_name)
            logger.info(f"Nova sessão criada para usuário {user_id}")
            
            return session
    
    def has_active_session(self, user_id: int) -> bool:
        """Verifica se o usuário tem uma sessão ativa"""
        with self.lock:
            if user_id not in self.sessions:
                return False
            
            session = self.sessions[user_id]
            
            # Verificar se a sessão expirou
            if time.time() - session.last_activity > SESSION_TIMEOUT:
                self._end_session(user_id)
                return False
            
            return session.is_active
    
    def get_session(self, user_id: int) -> Optional[UserSession]:
        """Retorna a sessão do usuário se ativa"""
        if self.has_active_session(user_id):
            return self.sessions[user_id]
        return None
    
    def update_session(self, user_id: int) -> bool:
        """Atualiza o timestamp da última atividade"""
        with self.lock:
            if user_id in self.sessions:
                self.sessions[user_id].last_activity = time.time()
                return True
            return False
    
    def add_message(self, user_id: int, role: str, content: str) -> bool:
        """Adiciona uma mensagem ao histórico da sessão"""
        with self.lock:
            if user_id not in self.sessions:
                return False
            
            message = {
                'role': role,
                'content': content,
                'timestamp': time.time()
            }
            
            self.sessions[user_id].messages.append(message)
            
            # Limitar histórico a 50 mensagens
            if len(self.sessions[user_id].messages) > 50:
                self.sessions[user_id].messages = self.sessions[user_id].messages[-50:]
            
            # Log de consulta médica se for mensagem do usuário
            if role == 'user':
                session = self.sessions[user_id]
                medical_context = session.medical_context
                urgency = medical_context.get('last_urgency', 'DESCONHECIDO')
                medical_logger.log_consultation(user_id, content, urgency)
            
            return True
    
    def get_session_history(self, user_id: int, limit: int = 10) -> List[Dict[str, Any]]:
        """Retorna o histórico de mensagens da sessão"""
        with self.lock:
            if user_id not in self.sessions:
                return []
            
            messages = self.sessions[user_id].messages
            return messages[-limit:] if limit > 0 else messages
    
    def update_medical_context(self, user_id: int, context_data: Dict[str, Any]) -> bool:
        """Atualiza o contexto médico da sessão"""
        with self.lock:
            if user_id not in self.sessions:
                return False
            
            self.sessions[user_id].medical_context.update(context_data)
            return True
    
    def get_medical_context(self, user_id: int) -> Dict[str, Any]:
        """Retorna o contexto médico da sessão"""
        with self.lock:
            if user_id not in self.sessions:
                return {}
            
            return self.sessions[user_id].medical_context.copy()
    
    def end_session(self, user_id: int) -> bool:
        """Finaliza a sessão do usuário"""
        with self.lock:
            return self._end_session(user_id)
    
    def _end_session(self, user_id: int) -> bool:
        """Finaliza a sessão (método interno)"""
        if user_id not in self.sessions:
            return False
        
        session = self.sessions[user_id]
        session.is_active = False
        
        # Calcular duração da sessão
        duration_minutes = int((time.time() - session.start_time) / 60)
        
        # Log do fim da sessão
        medical_logger.log_session_end(user_id, duration_minutes)
        logger.info(f"Sessão finalizada para usuário {user_id} (duração: {duration_minutes}min)")
        
        # Remover sessão após um tempo
        del self.sessions[user_id]
        
        return True
    
    def cleanup_expired_sessions(self) -> int:
        """Remove sessões expiradas"""
        with self.lock:
            current_time = time.time()
            expired_users = []
            
            for user_id, session in self.sessions.items():
                if current_time - session.last_activity > SESSION_TIMEOUT:
                    expired_users.append(user_id)
            
            for user_id in expired_users:
                self._end_session(user_id)
            
            if expired_users:
                logger.info(f"Removidas {len(expired_users)} sessões expiradas")
            
            return len(expired_users)
    
    def get_active_sessions_count(self) -> int:
        """Retorna o número de sessões ativas"""
        with self.lock:
            return len([s for s in self.sessions.values() if s.is_active])
    
    def get_session_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas das sessões"""
        with self.lock:
            total_sessions = len(self.sessions)
            active_sessions = self.get_active_sessions_count()
            
            if total_sessions > 0:
                avg_messages = sum(len(s.messages) for s in self.sessions.values()) / total_sessions
                avg_duration = sum(
                    (time.time() - s.start_time) for s in self.sessions.values()
                ) / total_sessions / 60  # em minutos
            else:
                avg_messages = 0
                avg_duration = 0
            
            return {
                'total_sessions': total_sessions,
                'active_sessions': active_sessions,
                'avg_messages_per_session': round(avg_messages, 2),
                'avg_duration_minutes': round(avg_duration, 2)
            }
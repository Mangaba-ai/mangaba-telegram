#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mangaba AI Core - Integração MCP + A2A
Sistema integrado de IA médica com Model Context Protocol e Agentes A2A
"""

import asyncio
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

from .gemini_client import GeminiMedicalAI
from .conversation_agents import ConversationManager, ConversationMode
from .quick_responses import QuickResponseEngine
from ..mcp.client import MCPClient, mcp_client
from ..medical.triage import MedicalTriage
from ..utils.session_manager import SessionManager

logger = logging.getLogger(__name__)

@dataclass
class MangabaAIResponse:
    """Resposta integrada do Mangaba AI"""
    content: str
    confidence: float
    source: str  # 'quick', 'ai', 'mcp', 'hybrid'
    emergency_level: int  # 0-5
    mcp_data: Optional[Dict[str, Any]] = None
    follow_up_questions: List[str] = None
    medical_resources: List[Dict[str, Any]] = None

class MangabaAICore:
    """Sistema central do Mangaba AI integrando MCP e A2A"""
    
    def __init__(self):
        """Inicializa o sistema Mangaba AI"""
        # Componentes A2A
        self.gemini_ai = GeminiMedicalAI()
        self.conversation_manager = ConversationManager()
        self.quick_response_engine = QuickResponseEngine()
        
        # Componentes médicos
        self.triage = MedicalTriage()
        self.session_manager = SessionManager()
        
        # Cliente MCP
        self.mcp_client = mcp_client
        
        # Estado do sistema
        self.mcp_enabled = True
        self.a2a_enabled = True
        
        logger.info("Mangaba AI Core inicializado com MCP + A2A")
    
    async def process_medical_query(
        self, 
        user_id: str, 
        message: str, 
        session_data: Optional[Dict] = None
    ) -> MangabaAIResponse:
        """Processa consulta médica usando sistema integrado MCP + A2A"""
        try:
            # 1. Análise inicial com A2A
            context = await self._build_integrated_context(user_id, message, session_data)
            
            # 2. Verificar se é emergência
            emergency_level = await self._assess_emergency_level(message, context)
            
            # 3. Tentar resposta rápida primeiro (A2A)
            quick_response = None
            if self.a2a_enabled:
                quick_response = await self._try_quick_response(user_id, message, context)
            
            # 4. Se não há resposta rápida, usar IA + MCP
            if not quick_response:
                ai_response = await self._generate_ai_response(user_id, message, context)
                mcp_data = await self._enrich_with_mcp(message, context) if self.mcp_enabled else None
                
                return MangabaAIResponse(
                    content=ai_response,
                    confidence=0.85,
                    source='hybrid' if mcp_data else 'ai',
                    emergency_level=emergency_level,
                    mcp_data=mcp_data,
                    follow_up_questions=await self._generate_follow_up(context),
                    medical_resources=mcp_data.get('resources', []) if mcp_data else []
                )
            else:
                # Enriquecer resposta rápida com MCP se necessário
                mcp_data = None
                if self.mcp_enabled and emergency_level > 2:
                    mcp_data = await self._enrich_with_mcp(message, context)
                
                return MangabaAIResponse(
                    content=quick_response,
                    confidence=0.95,
                    source='quick',
                    emergency_level=emergency_level,
                    mcp_data=mcp_data,
                    follow_up_questions=[],
                    medical_resources=mcp_data.get('resources', []) if mcp_data else []
                )
                
        except Exception as e:
            logger.error(f"Erro no processamento Mangaba AI: {e}")
            return MangabaAIResponse(
                content="Desculpe, ocorreu um erro interno. Tente novamente.",
                confidence=0.0,
                source='error',
                emergency_level=0
            )
    
    async def _build_integrated_context(
        self, 
        user_id: str, 
        message: str, 
        session_data: Optional[Dict]
    ) -> Dict[str, Any]:
        """Constrói contexto integrado A2A + MCP"""
        # Contexto A2A
        a2a_stats = self.conversation_manager.get_conversation_stats(user_id)
        
        # Dados da sessão
        session_info = session_data or self.session_manager.get_session(user_id)
        
        # Análise de triagem
        triage_data = self.triage.analyze_symptoms(message)
        
        return {
            'user_id': user_id,
            'message': message,
            'a2a_context': a2a_stats,
            'session_info': session_info,
            'triage_data': triage_data,
            'timestamp': asyncio.get_event_loop().time()
        }
    
    async def _assess_emergency_level(self, message: str, context: Dict) -> int:
        """Avalia nível de emergência (0-5)"""
        emergency_keywords = {
            5: ['parada cardíaca', 'não respira', 'inconsciente', 'overdose'],
            4: ['dor no peito', 'falta de ar severa', 'sangramento intenso'],
            3: ['febre alta', 'vômito persistente', 'dor intensa'],
            2: ['dor moderada', 'mal estar', 'tontura'],
            1: ['dor leve', 'desconforto', 'cansaço']
        }
        
        message_lower = message.lower()
        for level, keywords in emergency_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                return level
        
        return 0
    
    async def _try_quick_response(
        self, 
        user_id: str, 
        message: str, 
        context: Dict
    ) -> Optional[str]:
        """Tenta gerar resposta rápida com A2A"""
        try:
            response, needs_ai = await self.conversation_manager.process_message(
                user_id, message, context.get('triage_data')
            )
            # Se não precisa de IA, retorna a resposta rápida
            return response if not needs_ai else None
        except Exception as e:
            logger.warning(f"Erro na resposta rápida A2A: {e}")
            return None
    
    async def _generate_ai_response(
        self, 
        user_id: str, 
        message: str, 
        context: Dict
    ) -> str:
        """Gera resposta usando IA Gemini"""
        try:
            return await self.gemini_ai.process_medical_query(
                message, 
                context.get('session_info', {}),
                user_id
            )
        except Exception as e:
            logger.error(f"Erro na IA Gemini: {e}")
            return "Desculpe, não consegui processar sua consulta no momento."
    
    async def _enrich_with_mcp(
        self, 
        message: str, 
        context: Dict
    ) -> Optional[Dict[str, Any]]:
        """Enriquece resposta com dados MCP"""
        try:
            mcp_data = {}
            
            # Buscar recursos médicos
            resources = await self.mcp_client.get_medical_resources(message)
            if resources:
                mcp_data['resources'] = resources
            
            # Verificar protocolos de emergência se necessário
            triage_data = context.get('triage_data', {})
            if triage_data.get('symptoms'):
                protocols = await self.mcp_client.get_emergency_protocols(
                    triage_data['symptoms']
                )
                if protocols:
                    mcp_data['emergency_protocols'] = protocols
            
            # Buscar diretrizes médicas
            if triage_data.get('condition'):
                guidelines = await self.mcp_client.get_medical_guidelines(
                    triage_data['condition']
                )
                if guidelines:
                    mcp_data['guidelines'] = guidelines
            
            return mcp_data if mcp_data else None
            
        except Exception as e:
            logger.warning(f"Erro ao enriquecer com MCP: {e}")
            return None
    
    async def _generate_follow_up(self, context: Dict) -> List[str]:
        """Gera perguntas de follow-up inteligentes"""
        triage_data = context.get('triage_data', {})
        
        follow_ups = []
        
        if 'dor' in context.get('message', '').lower():
            follow_ups.extend([
                "Em uma escala de 1 a 10, qual a intensidade da dor?",
                "A dor é constante ou vem em ondas?",
                "Há quanto tempo você sente essa dor?"
            ])
        
        if 'febre' in context.get('message', '').lower():
            follow_ups.extend([
                "Você mediu a temperatura? Qual foi o valor?",
                "Há quanto tempo está com febre?",
                "Tem outros sintomas além da febre?"
            ])
        
        return follow_ups[:3]  # Máximo 3 perguntas
    
    async def log_interaction(
        self, 
        user_id: str, 
        query: str, 
        response: MangabaAIResponse
    ):
        """Registra interação para análise e melhoria"""
        try:
            event_data = {
                'user_id': user_id,
                'query': query,
                'response_source': response.source,
                'confidence': response.confidence,
                'emergency_level': response.emergency_level,
                'timestamp': asyncio.get_event_loop().time()
            }
            
            if self.mcp_enabled:
                await self.mcp_client.log_medical_event(event_data)
            
        except Exception as e:
            logger.warning(f"Erro ao registrar interação: {e}")
    
    def enable_mcp(self, enabled: bool = True):
        """Habilita/desabilita MCP"""
        self.mcp_enabled = enabled
        logger.info(f"MCP {'habilitado' if enabled else 'desabilitado'}")
    
    def enable_a2a(self, enabled: bool = True):
        """Habilita/desabilita A2A"""
        self.a2a_enabled = enabled
        logger.info(f"A2A {'habilitado' if enabled else 'desabilitado'}")
    
    async def get_system_status(self) -> Dict[str, Any]:
        """Retorna status do sistema Mangaba AI"""
        return {
            'mcp_enabled': self.mcp_enabled,
            'a2a_enabled': self.a2a_enabled,
            'mcp_connected': self.mcp_client.connected,
            'components': {
                'gemini_ai': bool(self.gemini_ai),
                'conversation_manager': bool(self.conversation_manager),
                'quick_response_engine': bool(self.quick_response_engine),
                'triage': bool(self.triage),
                'session_manager': bool(self.session_manager)
            }
        }

# Instância global do Mangaba AI Core
mangaba_ai_core = MangabaAICore()
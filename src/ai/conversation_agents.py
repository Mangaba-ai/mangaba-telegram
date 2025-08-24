#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agentes de Conversação A2A (Agent-to-Agent) - Médico de Bolso
Sistema de agentes inteligentes para conversação dinâmica e fluida
"""

import logging
import asyncio
import random
from typing import Dict, List, Optional, Tuple, Any
from dataclasses import dataclass
from enum import Enum
from src.ai.quick_responses import QuickResponseEngine

logger = logging.getLogger(__name__)

class ConversationMode(Enum):
    """Modos de conversação disponíveis"""
    QUICK = "quick"  # Respostas rápidas e diretas
    DETAILED = "detailed"  # Respostas detalhadas
    EMPATHETIC = "empathetic"  # Respostas empáticas
    CLINICAL = "clinical"  # Respostas clínicas
    EMERGENCY = "emergency"  # Modo emergência

@dataclass
class ConversationContext:
    """Contexto da conversação"""
    user_id: str
    message_count: int
    urgency_level: str
    symptoms: List[str]
    conversation_mode: ConversationMode
    last_response_time: float
    user_preferences: Dict[str, Any]
    session_duration: float

class ResponseAgent:
    """Agente responsável por gerar respostas dinâmicas"""
    
    def __init__(self):
        self.quick_responses = {
            "greeting": [
                "Olá! 👋 Como posso ajudar com sua saúde hoje?",
                "Oi! 🩺 Conte-me seus sintomas.",
                "Bem-vindo! 💙 O que está sentindo?"
            ],
            "pain": [
                "Entendo sua dor. 😔 Onde exatamente dói?",
                "Dor pode ser preocupante. 🤕 Me conte mais detalhes.",
                "Vamos avaliar essa dor. 📋 Intensidade de 1-10?"
            ],
            "fever": [
                "Febre precisa atenção! 🌡️ Qual a temperatura?",
                "Temperatura alta? 🔥 Há quanto tempo?",
                "Febre pode indicar infecção. 🦠 Outros sintomas?"
            ],
            "emergency": [
                "⚠️ URGENTE! Procure atendimento IMEDIATO!",
                "🚨 Vá ao hospital AGORA! Não espere!",
                "⛑️ EMERGÊNCIA! Chame 192 ou vá ao PS!"
            ]
        }
        
        self.conversation_starters = [
            "Me conte o que está acontecendo...",
            "Vamos conversar sobre seus sintomas...",
            "Estou aqui para ajudar. Descreva como se sente...",
            "Que sintomas você está apresentando?"
        ]
    
    def get_quick_response(self, category: str, context: ConversationContext) -> str:
        """Retorna resposta rápida baseada na categoria"""
        if category in self.quick_responses:
            responses = self.quick_responses[category]
            return random.choice(responses)
        return "Conte-me mais sobre isso... 🤔"
    
    def adapt_response_style(self, base_response: str, context: ConversationContext) -> str:
        """Adapta estilo da resposta baseado no contexto"""
        if context.conversation_mode == ConversationMode.QUICK:
            return self._make_response_concise(base_response)
        elif context.conversation_mode == ConversationMode.EMPATHETIC:
            return self._add_empathy(base_response)
        elif context.conversation_mode == ConversationMode.EMERGENCY:
            return self._add_urgency(base_response)
        return base_response
    
    def _make_response_concise(self, response: str) -> str:
        """Torna resposta mais concisa"""
        # Remove explicações longas, mantém o essencial
        sentences = response.split('. ')
        if len(sentences) > 2:
            return '. '.join(sentences[:2]) + '.'
        return response
    
    def _add_empathy(self, response: str) -> str:
        """Adiciona empatia à resposta"""
        empathy_starters = [
            "Entendo como deve estar se sentindo. ",
            "Sei que é preocupante. ",
            "Compreendo sua situação. "
        ]
        starter = random.choice(empathy_starters)
        return starter + response
    
    def _add_urgency(self, response: str) -> str:
        """Adiciona urgência à resposta"""
        return f"⚠️ IMPORTANTE: {response}"

class ContextAgent:
    """Agente responsável por gerenciar contexto da conversação"""
    
    def __init__(self):
        self.user_contexts: Dict[str, ConversationContext] = {}
        self.symptom_keywords = {
            "pain": ["dor", "doendo", "machuca", "ardendo"],
            "fever": ["febre", "temperatura", "quente", "calor"],
            "nausea": ["enjoo", "náusea", "vomito", "mal estar"],
            "breathing": ["respirar", "falta de ar", "sufoco", "ofegante"]
        }
    
    def get_or_create_context(self, user_id: str) -> ConversationContext:
        """Obtém ou cria contexto para usuário"""
        if user_id not in self.user_contexts:
            self.user_contexts[user_id] = ConversationContext(
                user_id=user_id,
                message_count=0,
                urgency_level="BAIXO",
                symptoms=[],
                conversation_mode=ConversationMode.QUICK,
                last_response_time=0.0,
                user_preferences={},
                session_duration=0.0
            )
        return self.user_contexts[user_id]
    
    def update_context(self, user_id: str, message: str, urgency_level: str = None):
        """Atualiza contexto baseado na mensagem"""
        context = self.get_or_create_context(user_id)
        context.message_count += 1
        
        # Detectar sintomas na mensagem
        detected_symptoms = self._detect_symptoms(message)
        context.symptoms.extend(detected_symptoms)
        
        # Atualizar nível de urgência se fornecido
        if urgency_level:
            context.urgency_level = urgency_level
            
        # Ajustar modo de conversação baseado na urgência
        if urgency_level in ["EMERGÊNCIA", "URGENTE"]:
            context.conversation_mode = ConversationMode.EMERGENCY
        elif context.message_count > 3:
            context.conversation_mode = ConversationMode.DETAILED
        else:
            context.conversation_mode = ConversationMode.QUICK
    
    def _detect_symptoms(self, message: str) -> List[str]:
        """Detecta sintomas na mensagem"""
        message_lower = message.lower()
        detected = []
        
        for symptom, keywords in self.symptom_keywords.items():
            if any(keyword in message_lower for keyword in keywords):
                detected.append(symptom)
        
        return detected

class FlowAgent:
    """Agente responsável por gerenciar fluxo da conversação"""
    
    def __init__(self):
        self.conversation_flows = {
            "initial": {
                "questions": [
                    "Qual é o principal sintoma que está sentindo?",
                    "Há quanto tempo isso começou?",
                    "A intensidade é leve, moderada ou forte?"
                ],
                "next_flow": "symptom_analysis"
            },
            "symptom_analysis": {
                "questions": [
                    "Esse sintoma piora com alguma atividade?",
                    "Você tomou algum medicamento?",
                    "Tem outros sintomas associados?"
                ],
                "next_flow": "recommendation"
            },
            "recommendation": {
                "questions": [
                    "Baseado no que me contou, recomendo...",
                    "Gostaria de mais alguma orientação?"
                ],
                "next_flow": "followup"
            }
        }
    
    def get_next_question(self, context: ConversationContext, current_flow: str = "initial") -> Optional[str]:
        """Retorna próxima pergunta baseada no fluxo"""
        if current_flow in self.conversation_flows:
            flow = self.conversation_flows[current_flow]
            questions = flow["questions"]
            
            # Selecionar pergunta baseada no número de mensagens
            question_index = min(context.message_count - 1, len(questions) - 1)
            if question_index >= 0:
                return questions[question_index]
        
        return None

class ConversationManager:
    """Gerenciador principal dos agentes de conversação"""
    
    def __init__(self):
        self.response_agent = ResponseAgent()
        self.context_agent = ContextAgent()
        self.flow_agent = FlowAgent()
        self.quick_response_engine = QuickResponseEngine()
        
    async def process_message(self, user_id: str, message: str, triage_data: Dict = None) -> Tuple[str, bool]:
        """Processa mensagem e retorna resposta dinâmica otimizada"""
        # Atualizar contexto
        urgency_level = triage_data.get('urgency_level') if triage_data else None
        self.context_agent.update_context(user_id, message, urgency_level)
        
        context = self.context_agent.get_or_create_context(user_id)
        
        # Primeiro: verificar respostas rápidas do novo sistema
        quick_response = self.quick_response_engine.get_contextual_response(message, context.message_count)
        
        if quick_response:
            # Se é emergência, sempre usar IA completa também
            if quick_response.urgency_level == "EMERGÊNCIA":
                return quick_response.response, True
            
            # Se requer IA completa, usar ambos
            if quick_response.requires_full_ai:
                return quick_response.response, True
            
            # Para respostas simples, usar apenas resposta rápida
            final_response = quick_response.response
            if quick_response.follow_up_question:
                final_response += f" {quick_response.follow_up_question}"
            
            return final_response, False
        
        # Verificar se é emergência pelo contexto
        if context.urgency_level in ["EMERGÊNCIA", "URGENTE"]:
            emergency_response = self.response_agent.get_quick_response("emergency", context)
            return emergency_response, True
        
        # Verificar palavras-chave de emergência
        if self.quick_response_engine.is_emergency_keyword(message):
            return "⚠️ Detectei preocupação em sua mensagem. Vou analisar cuidadosamente.", True
        
        # Detectar categoria da mensagem (sistema antigo como fallback)
        category = self._detect_message_category(message)
        
        # Para mensagens simples, usar resposta rápida do sistema antigo
        if category and context.message_count <= 2:
            quick_response = self.response_agent.get_quick_response(category, context)
            
            # Adicionar pergunta de follow-up
            follow_up = self.flow_agent.get_next_question(context)
            if follow_up:
                quick_response += f" {follow_up}"
            
            return quick_response, False
        
        # Para conversas mais complexas, usar IA completa
        return "", True
    
    def _detect_message_category(self, message: str) -> Optional[str]:
        """Detecta categoria da mensagem"""
        message_lower = message.lower()
        
        greetings = ["oi", "olá", "bom dia", "boa tarde", "boa noite"]
        if any(greeting in message_lower for greeting in greetings):
            return "greeting"
        
        pain_words = ["dor", "doendo", "machuca", "ardendo"]
        if any(word in message_lower for word in pain_words):
            return "pain"
        
        fever_words = ["febre", "temperatura", "quente"]
        if any(word in message_lower for word in fever_words):
            return "fever"
        
        return None
    
    def get_conversation_stats(self, user_id: str) -> Dict:
        """Retorna estatísticas da conversação"""
        context = self.context_agent.get_or_create_context(user_id)
        return {
            "message_count": context.message_count,
            "urgency_level": context.urgency_level,
            "symptoms": context.symptoms,
            "conversation_mode": context.conversation_mode.value
        }
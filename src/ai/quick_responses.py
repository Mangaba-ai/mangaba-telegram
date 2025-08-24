#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Respostas Rápidas - Médico de Bolso
Respostas instantâneas para consultas médicas comuns
"""

import logging
import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class QuickResponse:
    """Estrutura para respostas rápidas"""
    response: str
    follow_up_question: Optional[str] = None
    urgency_level: str = "BAIXO"
    requires_full_ai: bool = False

class QuickResponseEngine:
    """Motor de respostas rápidas para consultas comuns"""
    
    def __init__(self):
        self.response_patterns = self._initialize_patterns()
        self.common_medications = self._initialize_medications()
        self.symptom_responses = self._initialize_symptom_responses()
    
    def _initialize_patterns(self) -> Dict[str, QuickResponse]:
        """Inicializa padrões de respostas rápidas"""
        return {
            # Saudações
            r'\b(oi|olá|bom dia|boa tarde|boa noite)\b': QuickResponse(
                response="Olá! 👋 Sou o Médico de Bolso. Como posso ajudar com sua saúde hoje?",
                follow_up_question="Conte-me seus sintomas ou o que está sentindo."
            ),
            
            # Dor de cabeça
            r'\b(dor de cabeça|cefaleia|enxaqueca)\b': QuickResponse(
                response="Dor de cabeça pode ter várias causas. 🤕",
                follow_up_question="Intensidade de 1-10? Há quanto tempo? Tomou algum medicamento?",
                urgency_level="MODERADO"
            ),
            
            # Febre
            r'\b(febre|temperatura|febril)\b': QuickResponse(
                response="Febre indica que seu corpo está combatendo algo. 🌡️",
                follow_up_question="Qual a temperatura? Há outros sintomas como dor no corpo?",
                urgency_level="MODERADO"
            ),
            
            # Dor no peito - EMERGÊNCIA
            r'\b(dor no peito|dor torácica|peito doendo)\b': QuickResponse(
                response="🚨 DOR NO PEITO É EMERGÊNCIA! Procure atendimento IMEDIATO!",
                urgency_level="EMERGÊNCIA",
                requires_full_ai=True
            ),
            
            # Falta de ar - EMERGÊNCIA
            r'\b(falta de ar|dificuldade respirar|sufoco|ofegante)\b': QuickResponse(
                response="🚨 DIFICULDADE RESPIRATÓRIA! Vá ao hospital AGORA!",
                urgency_level="EMERGÊNCIA",
                requires_full_ai=True
            ),
            
            # Dor de garganta
            r'\b(dor de garganta|garganta inflamada|engolir dói)\b': QuickResponse(
                response="Dor de garganta é comum. 😷",
                follow_up_question="Há febre? Dificuldade para engolir? Há quanto tempo?",
                urgency_level="BAIXO"
            ),
            
            # Tosse
            r'\b(tosse|tossindo|pigarro)\b': QuickResponse(
                response="Tosse pode ser sinal de irritação ou infecção. 😷",
                follow_up_question="Tosse seca ou com catarro? Há febre? Há quanto tempo?",
                urgency_level="BAIXO"
            ),
            
            # Náusea/Vômito
            r'\b(náusea|enjoo|vômito|vomitando)\b': QuickResponse(
                response="Náusea pode ter várias causas. 🤢",
                follow_up_question="Vomitou? Há dor abdominal? Comeu algo diferente?",
                urgency_level="MODERADO"
            ),
            
            # Dor abdominal
            r'\b(dor na barriga|dor abdominal|estômago doendo)\b': QuickResponse(
                response="Dor abdominal precisa ser avaliada. 🤕",
                follow_up_question="Onde exatamente dói? Intensidade? Há náusea?",
                urgency_level="MODERADO",
                requires_full_ai=True
            ),
            
            # Diarreia
            r'\b(diarreia|diarréia|intestino solto)\b': QuickResponse(
                response="Diarreia pode causar desidratação. 💧",
                follow_up_question="Há sangue? Febre? Há quanto tempo? Está se hidratando?",
                urgency_level="MODERADO"
            ),
            
            # Insônia
            r'\b(insônia|não consigo dormir|sem sono)\b': QuickResponse(
                response="Problemas de sono afetam a saúde. 😴",
                follow_up_question="Há quanto tempo? Stress? Mudanças na rotina?",
                urgency_level="BAIXO"
            ),
            
            # Ansiedade
            r'\b(ansiedade|ansioso|nervoso|estresse)\b': QuickResponse(
                response="Ansiedade é comum, mas pode ser tratada. 💙",
                follow_up_question="Sintomas físicos? Palpitações? Há quanto tempo?",
                urgency_level="BAIXO"
            ),
            
            # Medicamentos
            r'\b(posso tomar|que medicamento|remédio para)\b': QuickResponse(
                response="⚠️ Não posso prescrever medicamentos.",
                follow_up_question="Consulte um médico ou farmacêutico para orientação segura.",
                requires_full_ai=True
            )
        }
    
    def _initialize_medications(self) -> Dict[str, str]:
        """Inicializa respostas sobre medicamentos comuns"""
        return {
            "paracetamol": "Paracetamol é seguro nas doses corretas. Siga a bula. 💊",
            "ibuprofeno": "Ibuprofeno é anti-inflamatório. Cuidado se tem problemas gástricos. 💊",
            "dipirona": "Dipirona é analgésico comum no Brasil. Respeite a dosagem. 💊",
            "aspirina": "Aspirina tem várias indicações. Consulte orientação médica. 💊"
        }
    
    def _initialize_symptom_responses(self) -> Dict[str, QuickResponse]:
        """Inicializa respostas para sintomas específicos"""
        return {
            "emergency_symptoms": QuickResponse(
                response="🚨 EMERGÊNCIA MÉDICA! Procure atendimento IMEDIATO!",
                urgency_level="EMERGÊNCIA"
            ),
            "urgent_symptoms": QuickResponse(
                response="⚠️ Sintoma preocupante. Procure atendimento médico hoje.",
                urgency_level="URGENTE"
            ),
            "moderate_symptoms": QuickResponse(
                response="Sintoma que merece atenção. 🩺",
                urgency_level="MODERADO"
            ),
            "mild_symptoms": QuickResponse(
                response="Sintoma comum, mas vamos avaliar. 😊",
                urgency_level="BAIXO"
            )
        }
    
    def find_quick_response(self, message: str) -> Optional[QuickResponse]:
        """Encontra resposta rápida para a mensagem"""
        message_lower = message.lower()
        
        # Verificar padrões de emergência primeiro
        emergency_patterns = [
            r'\b(dor no peito|infarto|ataque cardíaco)\b',
            r'\b(falta de ar severa|não consigo respirar)\b',
            r'\b(desmaiei|perdi consciência)\b',
            r'\b(sangramento intenso|muito sangue)\b',
            r'\b(convulsão|convulsões)\b'
        ]
        
        for pattern in emergency_patterns:
            if re.search(pattern, message_lower):
                return self.symptom_responses["emergency_symptoms"]
        
        # Verificar padrões normais
        for pattern, response in self.response_patterns.items():
            if re.search(pattern, message_lower):
                return response
        
        # Verificar medicamentos
        for med, response_text in self.common_medications.items():
            if med in message_lower:
                return QuickResponse(
                    response=response_text,
                    follow_up_question="Tem alguma alergia? Está tomando outros medicamentos?",
                    requires_full_ai=True
                )
        
        return None
    
    def get_contextual_response(self, message: str, conversation_count: int) -> Optional[QuickResponse]:
        """Retorna resposta contextual baseada no número de mensagens"""
        quick_response = self.find_quick_response(message)
        
        if quick_response:
            # Adaptar resposta baseada no contexto da conversa
            if conversation_count == 1:  # Primeira mensagem
                if quick_response.urgency_level != "EMERGÊNCIA":
                    quick_response.response += " Vou te ajudar a entender melhor."
            
            elif conversation_count > 3:  # Conversa longa
                quick_response.requires_full_ai = True  # Usar IA completa para análise detalhada
        
        return quick_response
    
    def is_emergency_keyword(self, message: str) -> bool:
        """Verifica se a mensagem contém palavras-chave de emergência"""
        emergency_keywords = [
            "emergência", "urgente", "grave", "sério", "preocupado",
            "dor forte", "muito mal", "piorando", "não aguento"
        ]
        
        message_lower = message.lower()
        return any(keyword in message_lower for keyword in emergency_keywords)
    
    def get_follow_up_suggestions(self, symptom_category: str) -> List[str]:
        """Retorna sugestões de perguntas de follow-up"""
        suggestions = {
            "pain": [
                "Qual a intensidade da dor de 1 a 10?",
                "A dor é constante ou vai e vem?",
                "Algo melhora ou piora a dor?"
            ],
            "fever": [
                "Mediu a temperatura? Qual valor?",
                "Há outros sintomas como dor no corpo?",
                "Tomou algum medicamento para febre?"
            ],
            "digestive": [
                "Há náusea ou vômito?",
                "Mudou algo na alimentação?",
                "A dor piora após comer?"
            ]
        }
        
        return suggestions.get(symptom_category, [
            "Pode me contar mais detalhes?",
            "Há quanto tempo isso começou?",
            "Tem outros sintomas?"
        ])
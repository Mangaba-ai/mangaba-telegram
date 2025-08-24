#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Triagem Médica - Médico de Bolso
Análise inicial de sintomas e classificação de urgência
"""

import re
import logging
from typing import Dict, List, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class TriageResult:
    """Resultado da triagem médica"""
    urgency_level: str
    symptoms_detected: List[str]
    risk_factors: List[str]
    recommendations: List[str]
    requires_immediate_attention: bool

class MedicalTriage:
    """Sistema de triagem médica para análise inicial de sintomas"""
    
    def __init__(self):
        """Inicializa o sistema de triagem"""
        self.emergency_keywords = {
            'dor_peito': ['dor no peito', 'dor torácica', 'aperto no peito', 'pressão no peito'],
            'respiracao': ['falta de ar', 'dificuldade respirar', 'sufocando', 'não consigo respirar'],
            'consciencia': ['desmaiei', 'perdi consciência', 'tonto', 'confuso', 'desorientado'],
            'sangramento': ['sangramento', 'hemorragia', 'sangue', 'sangrando muito'],
            'neurologico': ['paralisia', 'não consigo mover', 'fala alterada', 'convulsão'],
            'dor_intensa': ['dor insuportável', 'dor muito forte', 'dor terrível', 'dor 10']
        }
        
        self.warning_symptoms = {
            'febre_alta': ['febre alta', 'febre 39', 'febre 40', 'muito quente'],
            'vomito': ['vomitando', 'vômito', 'enjoo forte', 'não para de vomitar'],
            'dor_abdominal': ['dor na barriga', 'dor abdominal', 'dor no estômago'],
            'cefaleia': ['dor de cabeça forte', 'enxaqueca', 'cefaleia intensa'],
            'alteracao_visual': ['visão turva', 'não enxergo', 'vista embaçada']
        }
        
        self.common_symptoms = {
            'febre_baixa': ['febre', 'febril', 'temperatura'],
            'tosse': ['tosse', 'tossindo', 'pigarro'],
            'dor_garganta': ['dor de garganta', 'garganta inflamada'],
            'coriza': ['coriza', 'nariz entupido', 'escorrendo'],
            'dor_cabeca': ['dor de cabeça', 'cefaleia leve'],
            'cansaco': ['cansado', 'fadiga', 'sem energia'],
            'dor_muscular': ['dor muscular', 'dor no corpo', 'corpo dolorido']
        }
        
        logger.info("Sistema de triagem médica inicializado")
    
    def analyze_symptoms(self, user_message: str) -> Dict[str, Any]:
        """Analisa sintomas descritos pelo usuário"""
        try:
            message_lower = user_message.lower()
            
            # Detectar sintomas
            emergency_symptoms = self._detect_symptoms(message_lower, self.emergency_keywords)
            warning_symptoms = self._detect_symptoms(message_lower, self.warning_symptoms)
            common_symptoms = self._detect_symptoms(message_lower, self.common_symptoms)
            
            # Determinar nível de urgência
            urgency_level = self._determine_urgency(
                emergency_symptoms, warning_symptoms, common_symptoms
            )
            
            # Identificar fatores de risco
            risk_factors = self._identify_risk_factors(message_lower)
            
            # Gerar recomendações
            recommendations = self._generate_recommendations(
                urgency_level, emergency_symptoms, warning_symptoms
            )
            
            # Verificar se requer atenção imediata
            requires_immediate = len(emergency_symptoms) > 0
            
            all_symptoms = emergency_symptoms + warning_symptoms + common_symptoms
            
            result = {
                'urgency_level': urgency_level,
                'symptoms_detected': all_symptoms,
                'risk_factors': risk_factors,
                'recommendations': recommendations,
                'requires_immediate_attention': requires_immediate
            }
            
            logger.info(f"Triagem realizada: urgência {urgency_level}, sintomas: {len(all_symptoms)}")
            return result
            
        except Exception as e:
            logger.error(f"Erro na análise de triagem: {e}")
            return self._get_default_triage_result()
    
    def _detect_symptoms(self, message: str, symptom_dict: Dict[str, List[str]]) -> List[str]:
        """Detecta sintomas específicos na mensagem"""
        detected = []
        
        for symptom_category, keywords in symptom_dict.items():
            for keyword in keywords:
                if keyword in message:
                    detected.append(symptom_category)
                    break
        
        return detected
    
    def _determine_urgency(self, emergency: List[str], warning: List[str], common: List[str]) -> str:
        """Determina o nível de urgência baseado nos sintomas"""
        if emergency:
            return "EMERGÊNCIA"
        elif warning:
            return "URGENTE"
        elif common:
            return "MODERADO"
        else:
            return "BAIXO"
    
    def _identify_risk_factors(self, message: str) -> List[str]:
        """Identifica fatores de risco mencionados"""
        risk_factors = []
        
        risk_keywords = {
            'idade_avancada': ['idoso', 'terceira idade', '70 anos', '80 anos'],
            'gravidez': ['grávida', 'gestante', 'gravidez'],
            'diabetes': ['diabetes', 'diabético'],
            'hipertensao': ['pressão alta', 'hipertensão'],
            'cardiopatia': ['problema coração', 'cardíaco', 'infarto anterior'],
            'imunossupressao': ['imunidade baixa', 'transplantado', 'quimioterapia']
        }
        
        for risk_factor, keywords in risk_keywords.items():
            for keyword in keywords:
                if keyword in message:
                    risk_factors.append(risk_factor)
                    break
        
        return risk_factors
    
    def _generate_recommendations(self, urgency: str, emergency: List[str], warning: List[str]) -> List[str]:
        """Gera recomendações baseadas na urgência"""
        recommendations = []
        
        if urgency == "EMERGÊNCIA":
            recommendations.extend([
                "🚨 Por favor, PROCURE ATENDIMENTO MÉDICO IMEDIATO - sua segurança é prioridade!",
                "📞 Não hesite em chamar emergência (SAMU 192) - eles estão preparados para ajudá-lo(a)",
                "🏥 Dirija-se ao pronto-socorro mais próximo com cuidado e, se possível, acompanhado(a)",
                "💙 Mantenha-se calmo(a) - você está tomando a decisão certa ao buscar ajuda"
            ])
        
        elif urgency == "URGENTE":
            recommendations.extend([
                "⚠️ É importante que você procure atendimento médico ainda hoje - não deixe para depois",
                "🏥 Recomendo que vá a uma UPA ou pronto-socorro para uma avaliação cuidadosa",
                "📱 Enquanto isso, monitore seus sintomas com atenção e anote qualquer mudança",
                "🤝 Se possível, peça para alguém acompanhá-lo(a) - cuidado nunca é demais"
            ])
        
        elif urgency == "MODERADO":
            recommendations.extend([
                "🩺 Recomendo agendar uma consulta médica nas próximas 24-48 horas para uma avaliação tranquila",
                "💧 Cuide-se mantendo uma boa hidratação - beba água regularmente",
                "🛏️ Permita-se descansar adequadamente - seu corpo precisa de energia para se recuperar",
                "📝 Anote seus sintomas para compartilhar com o médico - isso ajudará muito no atendimento"
            ])
        
        else:  # BAIXO
            recommendations.extend([
                "📅 Quando conveniente, considere agendar uma consulta de rotina para acompanhamento",
                "💧 Continue cuidando bem de si - mantenha uma boa hidratação",
                "😴 Descanse quando necessário e continue observando como se sente",
                "🌟 Lembre-se: cuidar da saúde preventivamente é sempre uma escolha sábia"
            ])
        
        return recommendations
    
    def _get_default_triage_result(self) -> Dict[str, Any]:
        """Resultado padrão em caso de erro"""
        return {
            'urgency_level': 'MODERADO',
            'symptoms_detected': [],
            'risk_factors': [],
            'recommendations': [
                "🩺 Para sua tranquilidade, recomendo uma consulta médica para avaliação cuidadosa",
                "📱 Continue observando como se sente e anote qualquer mudança",
                "⚠️ Se os sintomas piorarem ou surgirem novas preocupações, não hesite em procurar atendimento",
                "💙 Lembre-se: cuidar da sua saúde é sempre a decisão mais acertada"
            ],
            'requires_immediate_attention': False
        }
    
    def get_urgency_color(self, urgency_level: str) -> str:
        """Retorna emoji de cor baseado na urgência"""
        colors = {
            'EMERGÊNCIA': '🔴',
            'URGENTE': '🟡',
            'MODERADO': '🟢',
            'BAIXO': '⚪'
        }
        return colors.get(urgency_level, '⚪')
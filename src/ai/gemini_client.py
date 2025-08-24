#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cliente Gemini AI - Médico de Bolso
Integração com Google Gemini para processamento de consultas médicas
Sistema de Fallback com múltiplas chaves de API e modelos
"""

import logging
import asyncio
import time
import google.generativeai as genai
from typing import List, Dict, Any, Optional, Tuple
from src.config.settings import GEMINI_API_KEYS, GEMINI_MODELS
from src.ai.conversation_agents import ConversationManager

logger = logging.getLogger(__name__)

class GeminiMedicalAI:
    """Cliente para integração com Gemini AI com sistema de fallback"""
    
    def __init__(self):
        """Inicializa o cliente Gemini com sistema de fallback"""
        self.api_keys = GEMINI_API_KEYS.copy()
        self.models = GEMINI_MODELS.copy()
        self.current_api_index = 0
        self.current_model_index = 0
        self.failed_combinations = set()  # Track failed API+Model combinations
        self.rate_limit_cooldowns = {}  # Track rate limit cooldowns
        self.medical_prompt = self._create_medical_prompt()
        
        # Initialize conversation manager for dynamic responses
        self.conversation_manager = ConversationManager()
        
        # Initialize first working combination
        self.current_client = None
        self._initialize_client()
        
        logger.info(f"Cliente Gemini AI inicializado com {len(self.api_keys)} chaves e {len(self.models)} modelos")
    
    def _initialize_client(self) -> bool:
        """Inicializa cliente com a primeira combinação disponível"""
        for api_idx, api_key in enumerate(self.api_keys):
            for model_idx, model_name in enumerate(self.models):
                combination = (api_idx, model_idx)
                
                # Skip failed combinations
                if combination in self.failed_combinations:
                    continue
                    
                # Check rate limit cooldown
                if self._is_rate_limited(combination):
                    continue
                
                try:
                    genai.configure(api_key=api_key)
                    self.current_client = genai.GenerativeModel(model_name)
                    self.current_api_index = api_idx
                    self.current_model_index = model_idx
                    
                    logger.info(f"Inicializado com API {api_idx+1} e modelo {model_name}")
                    return True
                    
                except Exception as e:
                    logger.warning(f"Falha ao inicializar API {api_idx+1} com modelo {model_name}: {e}")
                    self.failed_combinations.add(combination)
                    continue
        
        logger.error("Nenhuma combinação de API/modelo disponível")
        return False
    
    def _create_medical_prompt(self) -> str:
        """Cria o prompt base para consultas médicas com suporte a conversação dinâmica"""
        return """
Você é o "Médico de Bolso" 🩺, um assistente médico virtual inteligente especializado em triagem inicial.
Você tem personalidade acolhedora, é direto quando necessário e adapta seu estilo de comunicação ao contexto.

PERSONALIDADE E COMUNICAÇÃO:
- Seja EMPÁTICO e ACOLHEDOR sempre
- Adapte o tom: mais direto para emergências, mais detalhado para casos complexos
- Use linguagem simples e acessível
- Seja CONCISO quando solicitado (modo quick)
- Mantenha conversas FLUIDAS e NATURAIS

DIRETRIZES MÉDICAS:
1. TRIAGEM INICIAL apenas - nunca diagnósticos definitivos
2. Identifique URGÊNCIA e aja adequadamente
3. Recomende atendimento médico quando apropriado
4. Use perguntas inteligentes para entender sintomas
5. Seja CLARO sobre limitações

SINAIS DE EMERGÊNCIA (atendimento IMEDIATO):
🚨 Dor no peito intensa
🚨 Dificuldade respiratória severa
🚨 Perda de consciência
🚨 Sangramento intenso
🚨 Febre >39°C persistente
🚨 Sintomas neurológicos

ESTILO DE RESPOSTA:
- Use emojis apropriados (🩺💊⚠️🏥)
- Seja DIRETO em emergências
- Faça perguntas de follow-up inteligentes
- Mantenha conversas CURTAS e FLUIDAS
- Termine sempre com orientação médica

Lembre-se: Você é um assistente inteligente de triagem que se adapta ao usuário e à situação.
"""
    
    def _is_rate_limited(self, combination: Tuple[int, int]) -> bool:
        """Verifica se uma combinação está em cooldown por rate limit"""
        if combination not in self.rate_limit_cooldowns:
            return False
        
        cooldown_until = self.rate_limit_cooldowns[combination]
        if time.time() < cooldown_until:
            return True
        
        # Remove expired cooldown
        del self.rate_limit_cooldowns[combination]
        return False
    
    def _set_rate_limit_cooldown(self, combination: Tuple[int, int], cooldown_seconds: int = 60):
        """Define cooldown para uma combinação que atingiu rate limit"""
        self.rate_limit_cooldowns[combination] = time.time() + cooldown_seconds
        logger.warning(f"Rate limit atingido para API {combination[0]+1} modelo {self.models[combination[1]]}, cooldown de {cooldown_seconds}s")
    
    def _switch_to_next_combination(self) -> bool:
        """Muda para próxima combinação disponível"""
        current_combination = (self.current_api_index, self.current_model_index)
        
        # Mark current combination as failed
        self.failed_combinations.add(current_combination)
        
        # Try to find next working combination
        for api_idx, api_key in enumerate(self.api_keys):
            for model_idx, model_name in enumerate(self.models):
                combination = (api_idx, model_idx)
                
                # Skip current and failed combinations
                if combination == current_combination or combination in self.failed_combinations:
                    continue
                    
                # Check rate limit cooldown
                if self._is_rate_limited(combination):
                    continue
                
                try:
                    genai.configure(api_key=api_key)
                    self.current_client = genai.GenerativeModel(model_name)
                    self.current_api_index = api_idx
                    self.current_model_index = model_idx
                    
                    logger.info(f"Mudança para API {api_idx+1} e modelo {model_name}")
                    return True
                    
                except Exception as e:
                    logger.warning(f"Falha ao mudar para API {api_idx+1} com modelo {model_name}: {e}")
                    self.failed_combinations.add(combination)
                    continue
        
        logger.error("Nenhuma combinação alternativa disponível")
        return False
    
    async def process_medical_query(
        self, 
        user_message: str, 
        user_id: str = None,
        session_history: List[Dict[str, Any]] = None,
        triage_data: Dict[str, Any] = None
    ) -> str:
        """Processa consulta médica usando Gemini AI com sistema de fallback e agentes de conversação"""
        
        # Usar agentes de conversação para respostas dinâmicas
        if user_id:
            quick_response, needs_full_ai = await self.conversation_manager.process_message(
                user_id, user_message, triage_data
            )
            
            # Se não precisa da IA completa, retornar resposta rápida
            if not needs_full_ai:
                logger.info(f"Resposta rápida gerada para usuário {user_id}")
                return quick_response
        
        # Processar com IA completa para casos complexos
        max_retries = len(self.api_keys) * len(self.models)
        
        for attempt in range(max_retries):
            try:
                if not self.current_client:
                    if not self._initialize_client():
                        break
                
                # Construir contexto da conversa
                conversation_context = self._build_conversation_context(
                    user_message, session_history, triage_data, user_id
                )
                
                # Gerar resposta
                response = await self._generate_response_with_retry(conversation_context)
                
                if response:
                    # Adaptar resposta baseada no contexto do usuário
                    if user_id:
                        context = self.conversation_manager.context_agent.get_or_create_context(user_id)
                        response = self.conversation_manager.response_agent.adapt_response_style(response, context)
                    
                    return response
                    
            except Exception as e:
                logger.error(f"Erro na tentativa {attempt + 1}: {e}")
                
                # Try to switch to next combination
                if not self._switch_to_next_combination():
                    break
        
        logger.error("Todas as combinações de API/modelo falharam")
        return self._get_fallback_response()
    
    def _build_conversation_context(self, user_message: str, session_history: List[Dict], triage_data: Dict, user_id: str = None) -> str:
        """Constrói o contexto da conversa para o Gemini com informações dinâmicas"""
        context_parts = [self.medical_prompt]
        
        # Adicionar dados de triagem se disponíveis
        if triage_data:
            context_parts.append(f"\nDADOS DE TRIAGEM INICIAL:\n{self._format_triage_data(triage_data)}")
        
        # Adicionar histórico da sessão
        if session_history:
            context_parts.append("\nHISTÓRICO DA CONVERSA:")
            for msg in session_history[-5:]:  # Últimas 5 mensagens
                role = "Paciente" if msg['role'] == 'user' else "Médico de Bolso"
                context_parts.append(f"{role}: {msg['content']}")
        
        # Adicionar mensagem atual
        context_parts.append(f"\nMENSAGEM ATUAL DO PACIENTE:\n{user_message}")
        
        # Instrução final
        context_parts.append(
            "\nResponda como o Médico de Bolso, fornecendo orientação médica inicial apropriada."
        )
        
        # Adicionar informações de contexto dinâmico se disponível
        if user_id:
            context = self.conversation_manager.context_agent.get_or_create_context(user_id)
            stats = self.conversation_manager.get_conversation_stats(user_id)
            
            context_parts.append(f"\nCONTEXTO DA CONVERSA:")
            context_parts.append(f"Número de mensagens: {stats['message_count']}")
            context_parts.append(f"Nível de urgência atual: {stats['urgency_level']}")
            context_parts.append(f"Sintomas detectados: {', '.join(stats['symptoms']) if stats['symptoms'] else 'Nenhum'}")
            context_parts.append(f"Modo de conversa: {stats['conversation_mode']}")
            
            # Ajustar prompt baseado no modo de conversa
            if stats['conversation_mode'] == 'quick':
                context_parts.append("\nINSTRUÇÃO ESPECIAL: Forneça uma resposta CONCISA e DIRETA. Máximo 2-3 frases.")
            elif stats['conversation_mode'] == 'emergency':
                context_parts.append("\nINSTRUÇÃO ESPECIAL: SITUAÇÃO DE EMERGÊNCIA! Seja direto e enfático sobre a necessidade de atendimento imediato.")
        
        return "\n".join(context_parts)
    
    def _format_triage_data(self, triage_data: Dict) -> str:
        """Formata dados de triagem para o contexto"""
        if not triage_data:
            return "Nenhum dado de triagem disponível"
        
        formatted = []
        if 'urgency_level' in triage_data:
            formatted.append(f"Nível de urgência: {triage_data['urgency_level']}")
        if 'symptoms_detected' in triage_data:
            formatted.append(f"Sintomas detectados: {', '.join(triage_data['symptoms_detected'])}")
        if 'risk_factors' in triage_data:
            formatted.append(f"Fatores de risco: {', '.join(triage_data['risk_factors'])}")
        
        return "\n".join(formatted)
    
    async def _generate_response_with_retry(self, context: str) -> str:
        """Gera resposta com tratamento de rate limits e fallback"""
        try:
            response = await self.current_client.generate_content_async(context)
            
            if response and response.text:
                return self._format_response(response.text)
            else:
                logger.warning("Resposta vazia do modelo")
                return None
                
        except Exception as e:
            error_message = str(e).lower()
            current_combination = (self.current_api_index, self.current_model_index)
            
            # Check for rate limit errors
            if any(keyword in error_message for keyword in ['rate limit', 'quota', 'too many requests', '429']):
                logger.warning(f"Rate limit detectado: {e}")
                self._set_rate_limit_cooldown(current_combination, 300)  # 5 minutes cooldown
                return None
            
            # Check for quota exceeded
            elif any(keyword in error_message for keyword in ['quota exceeded', 'billing', 'credits']):
                logger.warning(f"Quota/créditos esgotados: {e}")
                self.failed_combinations.add(current_combination)
                return None
            
            # Check for authentication errors
            elif any(keyword in error_message for keyword in ['authentication', 'api key', 'unauthorized', '401']):
                logger.error(f"Erro de autenticação: {e}")
                self.failed_combinations.add(current_combination)
                return None
            
            # Other errors
            else:
                logger.error(f"Erro inesperado: {e}")
                return None
    
    async def _generate_response(self, context: str) -> str:
        """Gera resposta usando Gemini AI"""
        try:
            response = self.model.generate_content(context)
            
            if response.text:
                return self._format_response(response.text)
            else:
                logger.warning("Resposta vazia do Gemini AI")
                return self._get_fallback_response()
                
        except Exception as e:
            logger.error(f"Erro ao gerar resposta com Gemini: {e}")
            return self._get_fallback_response()
    
    def _format_response(self, response: str) -> str:
        """Formata a resposta do Gemini"""
        # Limitar tamanho da resposta
        if len(response) > 2000:
            response = response[:1950] + "\n\n[...resposta truncada...]"
        
        # Adicionar disclaimer se não estiver presente
        if "consulta médica" not in response.lower():
            response += "\n\n⚠️ *Lembre-se:* Esta é apenas uma orientação inicial. Consulte um médico para avaliação completa."
        
        return response
    
    def reset_failed_combinations(self):
        """Reseta combinações falhadas (útil para testes ou após resolver problemas)"""
        self.failed_combinations.clear()
        self.rate_limit_cooldowns.clear()
        logger.info("Combinações falhadas resetadas")
    
    def get_system_status(self) -> Dict[str, Any]:
        """Retorna status atual do sistema de fallback"""
        current_combination = (self.current_api_index, self.current_model_index)
        
        status = {
            "current_api": self.current_api_index + 1,
            "current_model": self.models[self.current_model_index],
            "total_apis": len(self.api_keys),
            "total_models": len(self.models),
            "failed_combinations": len(self.failed_combinations),
            "rate_limited_combinations": len([c for c in self.rate_limit_cooldowns.keys() if self._is_rate_limited(c)]),
            "available_combinations": 0
        }
        
        # Count available combinations
        for api_idx in range(len(self.api_keys)):
            for model_idx in range(len(self.models)):
                combination = (api_idx, model_idx)
                if combination not in self.failed_combinations and not self._is_rate_limited(combination):
                    status["available_combinations"] += 1
        
        return status
    
    def _get_fallback_response(self) -> str:
        """Retorna resposta de fallback quando AI não está disponível"""
        status = self.get_system_status()
        
        if status["available_combinations"] > 0:
            message = (
                "🤖 *Assistente Médico Temporariamente Indisponível*\n\n"
                "Estou enfrentando dificuldades técnicas no momento. "
                "Por favor, tente novamente em alguns minutos.\n\n"
            )
        else:
            message = (
                "🤖 *Assistente Médico Indisponível*\n\n"
                "Todos os serviços de IA estão temporariamente indisponíveis. "
                "Isso pode ser devido a limites de uso ou problemas técnicos.\n\n"
                "Por favor, tente novamente mais tarde.\n\n"
            )
        
        message += (
            "⚠️ **Em caso de emergência médica, procure atendimento presencial imediatamente "
            "ou ligue para o SAMU (192).**"
        )
        
        return message
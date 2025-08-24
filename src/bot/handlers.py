#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Handlers do Bot Telegram - Médico de Bolso
Gerencia comandos e mensagens dos usuários
"""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from src.config.settings import WELCOME_MESSAGE, HELP_MESSAGE, DISCLAIMER_MESSAGE
from src.ai.gemini_client import GeminiMedicalAI
from src.medical.triage import MedicalTriage
from src.utils.session_manager import SessionManager

logger = logging.getLogger(__name__)

# Instâncias globais
gemini_ai = GeminiMedicalAI()
medical_triage = MedicalTriage()
session_manager = SessionManager()

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /start"""
    try:
        user_id = update.effective_user.id
        user_name = update.effective_user.first_name or "Usuário"
        
        logger.info(f"Usuário {user_id} ({user_name}) iniciou uma sessão")
        
        # Inicializar sessão do usuário
        session_manager.create_session(user_id)
        
        # Enviar mensagem de boas-vindas
        await update.message.reply_text(
            f"Olá, {user_name}!\n\n{WELCOME_MESSAGE}",
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Enviar disclaimer médico
        await update.message.reply_text(
            DISCLAIMER_MESSAGE,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Erro no handler start: {e}")
        await update.message.reply_text(
            "❌ Ocorreu um erro ao iniciar o atendimento. Tente novamente."
        )

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /help"""
    try:
        await update.message.reply_text(
            HELP_MESSAGE,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Erro no handler help: {e}")
        await update.message.reply_text(
            "❌ Erro ao exibir ajuda. Tente novamente."
        )

async def status_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /status - mostra status do sistema de fallback"""
    try:
        # Obter status do sistema
        status = gemini_ai.get_system_status()
        
        status_message = (
            f"🤖 **Status do Sistema de IA - Tudo sob controle!**\n\n"
            f"📡 **API em uso:** {status['current_api']}/{status['total_apis']} (funcionando perfeitamente)\n"
            f"🧠 **Modelo ativo:** {status['current_model']} (pronto para ajudá-lo)\n\n"
            f"📊 **Informações técnicas:**\n"
            f"• ✅ Combinações disponíveis: {status['available_combinations']}\n"
            f"• ⚠️ Combinações com problemas: {status['failed_combinations']}\n"
            f"• ⏳ Aguardando liberação: {status['rate_limited_combinations']}\n\n"
        )
        
        if status['available_combinations'] > 0:
            status_message += "🟢 **Sistema funcionando perfeitamente - pronto para atendê-lo!**"
        elif status['rate_limited_combinations'] > 0:
            status_message += "🟡 **Sistema operacional com algumas limitações temporárias - ainda posso ajudá-lo!**"
        else:
            status_message += "🔴 **Sistema temporariamente indisponível - tente novamente em alguns minutos**"
        
        await update.message.reply_text(
            status_message,
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Erro no handler status: {e}")
        await update.message.reply_text(
            "❌ Ops! Não consegui verificar o status no momento. Tente novamente em instantes."
        )

async def reset_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler para o comando /reset - reseta combinações falhadas (admin)"""
    try:
        # Reset das combinações falhadas
        gemini_ai.reset_failed_combinations()
        
        await update.message.reply_text(
            "🔄 **Sistema Reiniciado com Sucesso!**\n\n"
            "✨ Todas as combinações foram resetadas com cuidado\n"
            "🔧 O sistema está novamente otimizado para oferecer o melhor atendimento\n"
            "💙 Pronto para ajudá-lo(a) com total eficiência!",
            parse_mode=ParseMode.MARKDOWN
        )
        
    except Exception as e:
        logger.error(f"Erro no handler reset: {e}")
        await update.message.reply_text(
            "❌ Ops! Não consegui reiniciar o sistema no momento. Tente novamente em instantes."
        )

async def medical_consultation_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler principal para consultas médicas"""
    try:
        user_id = update.effective_user.id
        user_message = update.message.text
        
        # Verificar se usuário tem sessão ativa
        if not session_manager.has_active_session(user_id):
            await update.message.reply_text(
                "😊 Olá! Parece que nossa conversa anterior expirou. \n\n"
                "Para sua segurança e para oferecer o melhor atendimento, use /start para iniciarmos uma nova consulta!"
            )
            return
        
        # Mostrar que o bot está processando
        await update.message.reply_chat_action("typing")
        
        # Adicionar mensagem do usuário ao histórico
        session_manager.add_message(user_id, "user", user_message)
        
        # Processar consulta médica
        response = await process_medical_consultation(user_id, user_message)
        
        # Adicionar resposta do bot ao histórico
        session_manager.add_message(user_id, "assistant", response)
        
        # Enviar resposta
        await update.message.reply_text(
            response,
            parse_mode=ParseMode.MARKDOWN
        )
        
        # Atualizar timestamp da sessão
        session_manager.update_session(user_id)
        
    except Exception as e:
        logger.error(f"Erro no handler de consulta médica: {e}")
        await update.message.reply_text(
            "❌ Ocorreu um erro ao processar sua consulta. Tente reformular sua pergunta."
        )

async def process_medical_consultation(user_id: int, user_message: str) -> str:
    """Processa consulta médica usando IA, triagem e conversação dinâmica"""
    try:
        # Obter histórico da sessão
        session_history = session_manager.get_session_history(user_id)
        
        # Análise de triagem inicial
        triage_result = medical_triage.analyze_symptoms(user_message)
        
        # Processar com Gemini AI usando conversação dinâmica
        ai_response = await gemini_ai.process_medical_query(
            user_message=user_message,
            user_id=str(user_id),  # Converter para string para compatibilidade
            session_history=session_history,
            triage_data=triage_result
        )
        
        return ai_response
        
    except Exception as e:
        logger.error(f"Erro ao processar consulta médica: {e}")
        return "❌ Não foi possível processar sua consulta no momento. Tente novamente em alguns instantes."
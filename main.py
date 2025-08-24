#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Médico de Bolso - Chatbot Médico para Telegram
Bot de atendimento médico inicial para triagem de sintomas

Powered by Mangaba AI - Sistema de IA Médica Avançado
"""

import asyncio
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Importações tradicionais (mantidas para compatibilidade)
from src.bot.handlers import start_handler, help_handler, medical_consultation_handler, status_handler, reset_handler
from src.config.settings import TELEGRAM_BOT_TOKEN
from src.utils.logger import setup_logger

# Demonstração do alias mangaba_ai (opcional para marketing)
# Você pode usar: import src as mangaba_ai
# E então: mangaba_ai.setup_logger(), mangaba_ai.start_handler, etc.
import src as mangaba_ai

# Configurar logging
setup_logger()
logger = logging.getLogger(__name__)

def demonstrar_mangaba_ai():
    """Demonstra o uso do alias mangaba_ai para fins de marketing"""
    print(f"🤖 Powered by {mangaba_ai.__description__}")
    print(f"📋 Versão: {mangaba_ai.__version__}")
    print(f"👥 Desenvolvido por: {mangaba_ai.__author__}")
    print("🚀 Tecnologias: Agentes A2A, Conversação Dinâmica, IA Médica")
    
    # Exemplo de uso alternativo com mangaba_ai
    # mangaba_ai.setup_logger()  # Equivale a setup_logger()
    # handlers = [mangaba_ai.start_handler, mangaba_ai.help_handler]  # Equivale às importações diretas

def main():
    """Função principal para inicializar o bot"""
    try:
        # Demonstrar branding Mangaba AI
        demonstrar_mangaba_ai()
        
        # Criar aplicação do bot
        application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
        
        # Adicionar handlers (pode usar mangaba_ai.start_handler alternativamente)
        application.add_handler(CommandHandler("start", start_handler))
        application.add_handler(CommandHandler("help", help_handler))
        application.add_handler(CommandHandler("status", status_handler))
        application.add_handler(CommandHandler("reset", reset_handler))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, medical_consultation_handler))
        
        logger.info("Médico de Bolso iniciado com sucesso!")
        
        # Iniciar o bot
        application.run_polling()
        
    except Exception as e:
        logger.error(f"Erro ao inicializar o bot: {e}")
        raise

if __name__ == "__main__":
    main()
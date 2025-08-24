# Médico de Bolso - Package initialization
# Marketing alias: mangaba_ai

# Importações principais para alias mangaba_ai
from .ai.gemini_client import GeminiMedicalAI
from .ai.conversation_agents import ConversationManager
from .ai.quick_responses import QuickResponseEngine
from .bot.handlers import (
    start_handler,
    help_handler, 
    medical_consultation_handler,
    status_handler,
    reset_handler
)
from .medical.triage import MedicalTriage
from .utils.session_manager import SessionManager
from .utils.logger import setup_logger
from .mcp.client import MCPClient, MCPMessage, MCPResponse, mcp_client

# Importação do Mangaba AI Core (MCP + A2A integrado)
from .ai.mangaba_ai_core import MangabaAICore, MangabaAIResponse, mangaba_ai_core

# Alias principal para marketing
__all__ = [
    # Mangaba AI Core (Sistema Integrado MCP + A2A)
    'MangabaAICore',
    'MangabaAIResponse', 
    'mangaba_ai_core',
    # IA e Conversação (A2A)
    'GeminiMedicalAI',
    'ConversationManager', 
    'QuickResponseEngine',
    # Sistema Médico
    'MedicalTriage',
    'SessionManager',
    # MCP (Model Context Protocol)
    'MCPClient',
    'MCPMessage',
    'MCPResponse',
    'mcp_client',
    # Utilitários
    'setup_logger',
    # Handlers do Bot
    'start_handler',
    'help_handler',
    'medical_consultation_handler', 
    'status_handler',
    'reset_handler'
]

# Versão do mangaba_ai
__version__ = '1.0.0'
__author__ = 'Mangaba AI Team'
__description__ = 'Sistema de IA Médica Avançado para Telegram'
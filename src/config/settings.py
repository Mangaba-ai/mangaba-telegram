#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configurações do Médico de Bolso
Gerencia variáveis de ambiente e configurações do sistema
"""

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Configurações do Telegram
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TELEGRAM_BOT_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN não encontrado nas variáveis de ambiente")

# Configurações do Gemini AI - Sistema de Fallback
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_KEY_2 = os.getenv('GEMINI_API_KEY_2')
GEMINI_API_KEY_3 = os.getenv('GEMINI_API_KEY_3')
GEMINI_API_KEY_4 = os.getenv('GEMINI_API_KEY_4')
GEMINI_API_KEY_5 = os.getenv('GEMINI_API_KEY_5')

# Lista de chaves de API para fallback
GEMINI_API_KEYS = [
    key for key in [
        GEMINI_API_KEY,
        GEMINI_API_KEY_2, 
        GEMINI_API_KEY_3,
        GEMINI_API_KEY_4,
        GEMINI_API_KEY_5
    ] if key is not None
]

if not GEMINI_API_KEYS:
    raise ValueError("Pelo menos uma GEMINI_API_KEY deve ser configurada")

# Modelos Gemini disponíveis para fallback
GEMINI_MODELS = [
    'gemini-2.5-pro',
    'gemini-2.5-flash', 
    'gemini-2.5-flash-lite',
    'gemini-live-2.5-flash-preview'
]

# Configurações MCP
MCP_SERVER_URL = os.getenv('MCP_SERVER_URL', 'http://localhost:8080')
MCP_API_KEY = os.getenv('MCP_API_KEY')

# Configurações de logging
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = os.getenv('LOG_FILE', 'medico_bolso.log')

# Configurações médicas
MAX_CONSULTATION_LENGTH = int(os.getenv('MAX_CONSULTATION_LENGTH', '2000'))
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', '1800'))  # 30 minutos

# Mensagens do sistema
WELCOME_MESSAGE = """
🏥 *Olá! Seja muito bem-vindo(a) ao Médico de Bolso!* 😊

É um prazer tê-lo(a) aqui! Sou seu assistente médico virtual, criado especialmente para ajudá-lo(a) com cuidado e atenção na triagem inicial de seus sintomas.

💙 *Estou aqui para:*
- Ouvir suas preocupações com atenção
- Fazer perguntas cuidadosas sobre seus sintomas
- Oferecer orientações médicas precisas e confiáveis
- Acompanhá-lo(a) com carinho durante nossa conversa

⚠️ *Com todo carinho, preciso lembrá-lo(a):* 
- Ofereço orientação inicial qualificada, mas não substituo uma consulta presencial
- Em situações de emergência, procure atendimento médico imediatamente
- Sua saúde é preciosa e merece o melhor cuidado!

Fique à vontade para me contar como está se sentindo. Estou aqui para ajudá-lo(a)! 🌟
"""

HELP_MESSAGE = """
🤗 *Fico feliz em ajudá-lo(a)! Aqui está como podemos conversar:*

✨ *Nosso processo de cuidado:*
1️⃣ Conte-me sobre seus sintomas - sem pressa, com todos os detalhes que achar importantes
2️⃣ Farei algumas perguntas carinhosas para entender melhor sua situação
3️⃣ Oferecerei orientações médicas precisas e recomendações cuidadosas

🛠️ *Comandos que podem ajudá-lo(a):*
/start - Começar nossa conversa
/help - Ver estas orientações novamente
/status - Verificar se tudo está funcionando bem
/reset - Reiniciar em caso de algum problema técnico

💝 *Lembre-se sempre:* 
Estou aqui para oferecer o melhor cuidado inicial possível, mas nada substitui o olhar atento de um médico presencial. Sua saúde merece atenção profissional completa!

Estou pronto(a) para ouvi-lo(a) com toda atenção! 💙
"""

DISCLAIMER_MESSAGE = """
💙 *CUIDADO MÉDICO RESPONSÁVEL - Informações Importantes:*

Com todo carinho e responsabilidade, preciso esclarecer que ofereço orientações médicas iniciais qualificadas, baseadas em conhecimento científico atualizado.

🏥 *Para seu bem-estar, é importante saber que:*
• Forneço triagem inicial e orientações gerais confiáveis
• Não substituo a avaliação presencial de um médico
• Cada pessoa é única e merece atenção médica personalizada
• Diagnósticos definitivos requerem exame clínico presencial

🚨 *Por favor, procure atendimento médico IMEDIATO se apresentar:*
• Dor no peito ou dificuldade para respirar
• Perda de consciência ou desmaios
• Sangramento intenso ou descontrolado
• Sintomas graves que pioram rapidamente
• Qualquer situação que cause preocupação intensa

✨ *Meu compromisso com você:*
Vou oferecer o melhor cuidado inicial possível, sempre com precisão científica e atenção humana. Sua saúde é preciosa!

Ao continuar, você confirma que compreende estas orientações importantes.
"""
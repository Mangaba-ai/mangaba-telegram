# 🏥 Mangaba AI - Sistema Integrado MCP + A2A

## 📋 Visão Geral

O **Mangaba AI** é um sistema avançado de inteligência artificial médica que integra duas tecnologias de ponta:

- **🔗 MCP (Model Context Protocol)**: Para acesso a recursos médicos externos e protocolos atualizados
- **🤖 A2A (Agent-to-Agent)**: Para conversação dinâmica e respostas rápidas

## 🚀 Características Principais

### 🎯 Sistema Integrado
- **MangabaAICore**: Núcleo que combina MCP e A2A de forma inteligente
- **Processamento Híbrido**: Usa respostas rápidas quando possível, IA completa quando necessário
- **Enriquecimento Automático**: Dados MCP são adicionados automaticamente em casos complexos
- **Detecção de Emergência**: Avaliação automática de urgência (0-5)

### 🔗 Componentes MCP
- **MCPClient**: Cliente para comunicação com servidores MCP
- **Recursos Médicos**: Acesso a bases de dados médicas atualizadas
- **Protocolos de Emergência**: Diretrizes para situações críticas
- **Interações Medicamentosas**: Verificação de compatibilidade
- **Logging Médico**: Registro de eventos para análise

### 🤖 Componentes A2A
- **GeminiMedicalAI**: IA médica baseada no Gemini
- **ConversationManager**: Gerenciamento de contexto e fluxo
- **QuickResponseEngine**: Respostas rápidas para consultas comuns
- **Agentes Especializados**: ResponseAgent, ContextAgent, FlowAgent

## 📦 Instalação e Uso

### Importação via Alias

```python
# Importar tudo via mangaba_ai
from src import mangaba_ai

# Usar o sistema integrado
core = mangaba_ai.mangaba_ai_core
response = await core.process_medical_query(
    user_id="user123",
    message="Estou com dor de cabeça"
)
```

### Componentes Disponíveis

```python
# Sistema Integrado (Recomendado)
mangaba_ai.MangabaAICore          # Classe principal
mangaba_ai.MangabaAIResponse      # Resposta estruturada
mangaba_ai.mangaba_ai_core        # Instância global

# Componentes A2A
mangaba_ai.GeminiMedicalAI        # IA médica
mangaba_ai.ConversationManager    # Gerenciador de conversação
mangaba_ai.QuickResponseEngine    # Respostas rápidas

# Componentes MCP
mangaba_ai.MCPClient              # Cliente MCP
mangaba_ai.MCPMessage             # Mensagem MCP
mangaba_ai.MCPResponse            # Resposta MCP
mangaba_ai.mcp_client             # Instância global

# Sistema Médico
mangaba_ai.MedicalTriage          # Triagem médica
mangaba_ai.SessionManager         # Gerenciador de sessões

# Handlers do Bot
mangaba_ai.start_handler          # Handler /start
mangaba_ai.help_handler           # Handler /help
mangaba_ai.medical_consultation_handler  # Handler consultas
mangaba_ai.status_handler         # Handler /status
mangaba_ai.reset_handler          # Handler /reset

# Utilitários
mangaba_ai.setup_logger           # Configuração de logs
```

## 🔧 Configuração

### Variáveis de Ambiente

```bash
# Configuração do Gemini
GEMINI_API_KEY=sua_chave_gemini

# Configuração do MCP
MCP_SERVER_URL=https://mcp-server.exemplo.com
MCP_API_KEY=sua_chave_mcp

# Configuração do Telegram
TELEGRAM_BOT_TOKEN=seu_token_telegram
```

### Inicialização

```python
import asyncio
from src import mangaba_ai

async def inicializar_sistema():
    # O sistema é inicializado automaticamente
    core = mangaba_ai.mangaba_ai_core
    
    # Verificar status
    status = await core.get_system_status()
    print(f"MCP: {'✅' if status['mcp_enabled'] else '❌'}")
    print(f"A2A: {'✅' if status['a2a_enabled'] else '❌'}")
    
    return core
```

## 🎯 Exemplos de Uso

### 1. Consulta Médica Básica

```python
async def consulta_basica():
    core = mangaba_ai.mangaba_ai_core
    
    response = await core.process_medical_query(
        user_id="user123",
        message="Tenho dor de cabeça há 2 dias"
    )
    
    print(f"Resposta: {response.content}")
    print(f"Fonte: {response.source}")  # 'quick', 'ai', 'mcp', 'hybrid'
    print(f"Confiança: {response.confidence}")
    print(f"Emergência: {response.emergency_level}/5")
```

### 2. Uso Direto do MCP

```python
async def usar_mcp_direto():
    mcp = mangaba_ai.mcp_client
    
    # Conectar
    await mcp.connect()
    
    # Buscar recursos
    recursos = await mcp.get_medical_resources("diabetes")
    
    # Verificar interações
    interacoes = await mcp.get_drug_interactions(["aspirina", "warfarina"])
    
    # Protocolos de emergência
    protocolos = await mcp.get_emergency_protocols(["dor no peito"])
    
    await mcp.disconnect()
```

### 3. Configuração Personalizada

```python
async def configuracao_personalizada():
    core = mangaba_ai.mangaba_ai_core
    
    # Desabilitar MCP temporariamente
    core.enable_mcp(False)
    
    # Processar apenas com A2A
    response = await core.process_medical_query(
        user_id="user123",
        message="Como prevenir gripe?"
    )
    
    # Reabilitar MCP
    core.enable_mcp(True)
```

### 4. Bot Telegram Integrado

```python
from telegram.ext import Application
from src import mangaba_ai

def criar_bot():
    app = Application.builder().token("SEU_TOKEN").build()
    
    # Usar handlers do mangaba_ai
    app.add_handler(mangaba_ai.start_handler)
    app.add_handler(mangaba_ai.help_handler)
    app.add_handler(mangaba_ai.medical_consultation_handler)
    app.add_handler(mangaba_ai.status_handler)
    app.add_handler(mangaba_ai.reset_handler)
    
    return app
```

## 📊 Estrutura de Resposta

### MangabaAIResponse

```python
@dataclass
class MangabaAIResponse:
    content: str                    # Resposta principal
    confidence: float               # Confiança (0.0-1.0)
    source: str                     # 'quick', 'ai', 'mcp', 'hybrid'
    emergency_level: int            # Urgência (0-5)
    mcp_data: Optional[Dict]        # Dados MCP (se disponível)
    follow_up_questions: List[str]  # Perguntas de acompanhamento
    medical_resources: List[Dict]   # Recursos médicos relacionados
```

### Níveis de Emergência

- **0**: Sem urgência (informações gerais)
- **1**: Baixa urgência (desconforto leve)
- **2**: Urgência moderada (sintomas incômodos)
- **3**: Urgência alta (sintomas preocupantes)
- **4**: Urgência crítica (sintomas graves)
- **5**: Emergência máxima (risco de vida)

## 🔄 Fluxo de Processamento

1. **Análise Inicial**: Contexto A2A + dados da sessão
2. **Avaliação de Emergência**: Classificação 0-5
3. **Tentativa de Resposta Rápida**: A2A primeiro
4. **IA Completa**: Se resposta rápida não for suficiente
5. **Enriquecimento MCP**: Dados externos quando necessário
6. **Geração de Follow-up**: Perguntas inteligentes
7. **Logging**: Registro para análise e melhoria

## 🛠️ Desenvolvimento e Extensão

### Adicionando Novos Agentes A2A

```python
from src.ai.conversation_agents import BaseAgent

class MeuAgente(BaseAgent):
    def process(self, message: str, context: Dict) -> str:
        # Sua lógica aqui
        return "Resposta personalizada"

# Registrar no ConversationManager
manager = mangaba_ai.ConversationManager()
manager.add_agent("meu_agente", MeuAgente())
```

### Estendendo Funcionalidades MCP

```python
class MCPExtendido(mangaba_ai.MCPClient):
    async def minha_funcao_personalizada(self, parametros):
        # Sua extensão aqui
        return await self._send_message({
            "action": "custom_action",
            "params": parametros
        })
```

## 📈 Monitoramento e Análise

### Métricas Disponíveis

```python
async def obter_metricas():
    core = mangaba_ai.mangaba_ai_core
    
    # Status do sistema
    status = await core.get_system_status()
    
    # Logs de interação (via MCP)
    if status['mcp_enabled']:
        # Dados são automaticamente enviados para análise
        pass
```

### Logs Estruturados

- **Consultas processadas**: Quantidade e tipos
- **Fontes de resposta**: Distribuição quick/ai/mcp/hybrid
- **Níveis de emergência**: Frequência por categoria
- **Performance**: Tempos de resposta
- **Erros**: Falhas e recuperações

## 🔒 Segurança e Privacidade

### Proteção de Dados
- **Anonimização**: IDs de usuário não identificáveis
- **Criptografia**: Comunicação segura com MCP
- **Logs Limitados**: Apenas dados necessários para melhoria
- **Conformidade**: Seguindo padrões médicos

### Boas Práticas
- **Validação de Entrada**: Sanitização de mensagens
- **Rate Limiting**: Controle de uso por usuário
- **Fallbacks**: Respostas seguras em caso de erro
- **Disclaimers**: Avisos sobre limitações médicas

## 🚀 Roadmap

### Próximas Funcionalidades
- [ ] **Integração com mais provedores MCP**
- [ ] **Agentes A2A especializados por área médica**
- [ ] **Interface web para monitoramento**
- [ ] **API REST para integração externa**
- [ ] **Suporte a múltiplos idiomas**
- [ ] **Análise de sentimento avançada**
- [ ] **Integração com prontuários eletrônicos**

## 📞 Suporte

### Documentação Adicional
- `CONVERSACAO_DINAMICA.md`: Detalhes dos agentes A2A
- `MANGABA_AI.md`: Documentação do alias de marketing
- `exemplo_mangaba_ai_integrado.py`: Exemplos práticos

### Contato
- **Autor**: Mangaba AI Team
- **Versão**: 1.0.0
- **Licença**: MIT

---

**🏥 Mangaba AI - Revolucionando o atendimento médico com IA avançada**

*Powered by MCP + A2A Integration*
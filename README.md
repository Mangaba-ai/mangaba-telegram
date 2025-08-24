# 🏥 Médico de Bolso - Mangaba AI

**Sistema médico inteligente com IA avançada, MCP e A2A**

Um assistente médico virtual revolucionário que combina IA Gemini, Model Context Protocol (MCP) e sistema Agent-to-Agent (A2A) para triagem médica inteligente via Telegram.

## 🚀 Características Principais

- 🤖 **Bot Telegram Inteligente**: Interface amigável e intuitiva
- 🧠 **IA Gemini Avançada**: Processamento médico de última geração
- 🔗 **MCP Integration**: Acesso a recursos médicos externos
- ⚡ **Sistema A2A**: Respostas rápidas e conversação dinâmica
- 🩺 **Triagem Automática**: Análise inteligente de sintomas e urgência
- 🚨 **Detecção de Emergência**: Avaliação automática de criticidade (0-5)
- 📊 **Mangaba AI Core**: Sistema integrado MCP + A2A
- 🔒 **Segurança Médica**: Logs estruturados e proteção de dados
- 🌐 **Português Brasileiro**: Otimizado para nossa realidade médica

## ⚠️ Aviso Médico Importante

**Este bot é apenas para triagem inicial e orientação geral. NÃO substitui consulta médica profissional.**

- ❌ Não fornece diagnósticos definitivos
- ❌ Não substitui atendimento médico presencial
- ✅ Orienta sobre sintomas e urgência
- ✅ Recomenda quando procurar ajuda médica

## 📁 Estrutura do Projeto

```
mangaba-telegram/
├── src/                    # Código fonte principal
│   ├── ai/                # Módulos de IA (Gemini, MCP, A2A)
│   │   ├── mangaba_ai_core.py  # Sistema integrado MCP + A2A
│   │   ├── conversation_agents.py  # Agentes de conversação
│   │   └── quick_responses.py      # Respostas rápidas
│   ├── mcp/               # Model Context Protocol
│   ├── telegram/          # Bot Telegram
│   └── __init__.py        # Exports principais (mangaba_ai)
├── docs/                  # Documentação
│   ├── MANGABA_AI_MCP_A2A.md      # Sistema integrado
│   ├── CONVERSACAO_DINAMICA.md    # Sistema A2A
│   └── MANGABA_AI.md              # Documentação geral
├── examples/              # Exemplos de uso
│   └── exemplo_mangaba_ai_integrado.py
├── main.py               # Ponto de entrada principal
├── requirements.txt      # Dependências
└── .env                 # Configurações (criar a partir do .env.example)
```

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Token do Bot Telegram (obtido via @BotFather)
- Chave da API Google Gemini
- Conexão com internet

## 🛠️ Instalação Completa (Passo a Passo)

### Passo 1: Preparar o Ambiente

#### 1.1 Verificar Python
```bash
# Verificar se Python está instalado (versão 3.8+)
python --version
# ou
python3 --version
```

#### 1.2 Baixar o Projeto
```bash
# Opção 1: Clone via Git (se tiver Git instalado)
git clone https://github.com/seu-usuario/medico-de-bolso.git
cd medico-de-bolso

# Opção 2: Download direto (se não tiver Git)
# Baixe o ZIP do GitHub e extraia em uma pasta
# Navegue até a pasta extraída
```

### Passo 2: Configurar Ambiente Virtual

#### 2.1 Criar Ambiente Virtual
```bash
# Windows
python -m venv venv

# Linux/Mac
python3 -m venv venv
```

#### 2.2 Ativar Ambiente Virtual
```bash
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

**✅ Verificação**: Após ativar, você deve ver `(venv)` no início da linha de comando.

### Passo 3: Instalar Dependências

#### 3.1 Atualizar pip
```bash
python -m pip install --upgrade pip
```

#### 3.2 Instalar Dependências do Projeto
```bash
pip install -r requirements.txt
```

**⏳ Aguarde**: Este processo pode levar alguns minutos.

### Passo 4: Obter Credenciais Necessárias

#### 4.1 Criar Bot no Telegram
1. **Abra o Telegram** e procure por `@BotFather`
2. **Inicie conversa** com `/start`
3. **Crie novo bot** com `/newbot`
4. **Escolha um nome** para seu bot (ex: "Meu Médico de Bolso")
5. **Escolha um username** único (ex: "meu_medico_bolso_bot")
6. **Copie o token** que aparece (formato: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### 4.2 Obter Chave do Google Gemini
1. **Acesse**: https://makersuite.google.com/app/apikey
2. **Faça login** com sua conta Google
3. **Clique em "Create API Key"**
4. **Copie a chave** gerada (formato: `AIzaSyC...`)

### Passo 5: Configurar Variáveis de Ambiente

#### 5.1 Copiar Arquivo de Exemplo
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

#### 5.2 Editar Arquivo .env
**Abra o arquivo `.env` em um editor de texto** e configure:

```env
# ========== OBRIGATÓRIO ==========
# Token do seu bot Telegram (obtido do @BotFather)
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz

# Chave principal da API Google Gemini (obtida do Google AI Studio)
GEMINI_API_KEY=AIzaSyC...

# ========== SISTEMA DE FALLBACK (OPCIONAL) ==========
# Chaves adicionais para alta disponibilidade
# Configure quantas quiser (até 5 total)
GEMINI_API_KEY_2=AIzaSyD...
GEMINI_API_KEY_3=AIzaSyE...
GEMINI_API_KEY_4=AIzaSyF...
GEMINI_API_KEY_5=AIzaSyG...

# ========== OUTRAS CONFIGURAÇÕES OPCIONAIS ==========
# Configurações de logging
LOG_LEVEL=INFO
LOG_FILE=medico_bolso.log

# Configurações de sessão
SESSION_TIMEOUT=1800
MAX_CONSULTATION_LENGTH=2000

# Configurações MCP (deixe como está se não souber)
MCP_SERVER_URL=http://localhost:8080
MCP_API_KEY=

# Configurações médicas
EMERGENCY_KEYWORDS=dor no peito,falta de ar,desmaio
WARNING_KEYWORDS=febre alta,vômito,dor intensa
```

**⚠️ IMPORTANTE**: 
- Substitua `123456789:ABCdefGHIjklMNOpqrsTUVwxyz` pelo seu token real
- Substitua `AIzaSyC...` pela sua chave Gemini real
- **NÃO compartilhe** este arquivo `.env` com ninguém

#### 5.3 Sistema de Fallback (Recomendado)

**🔄 Por que usar múltiplas chaves API?**
- **Alta Disponibilidade**: Se uma API atingir limite, o bot continua funcionando
- **Distribuição de Carga**: Reduz chance de atingir rate limits
- **Redundância**: Proteção contra falhas temporárias

**📝 Como obter múltiplas chaves:**
1. Acesse [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Crie projetos diferentes ou use contas diferentes
3. Gere uma chave API para cada projeto
4. Configure no arquivo `.env`

**⚙️ Como funciona:**
- O bot usa `GEMINI_API_KEY` como principal
- Se falhar, tenta `GEMINI_API_KEY_2`, depois `GEMINI_API_KEY_3`, etc.
- Detecta automaticamente rate limits e quotas esgotadas
- Aplica cooldown temporário em APIs com problemas
- Use `/status` para monitorar o sistema
- Use `/reset` para resetar falhas temporárias

### Passo 6: Testar a Configuração

#### 6.1 Verificar Dependências
```bash
python run.py
```

**✅ Se tudo estiver correto**, você verá:
```
🏥 MÉDICO DE BOLSO - INICIANDO...
✅ Arquivo .env encontrado
✅ Variáveis obrigatórias configuradas
✅ Dependências instaladas
✅ Diretórios criados
🚀 Bot iniciado com sucesso!
```

#### 6.2 Executar o Bot
```bash
# Opção 1: Execução simples
python main.py

# Opção 2: Execução com verificações (recomendado)
python run.py
```

**✅ Bot funcionando**: Você verá mensagens como:
```
2024-01-20 10:30:00 - INFO - Bot iniciado com sucesso
2024-01-20 10:30:00 - INFO - Aguardando mensagens...
```

## 🚀 Como Usar o Bot

### Passo 7: Testar o Bot no Telegram

#### 7.1 Encontrar seu Bot
1. **Abra o Telegram** no celular ou computador
2. **Procure pelo username** do seu bot (ex: `@meu_medico_bolso_bot`)
3. **Clique no bot** nos resultados da busca
4. **Clique em "INICIAR"** ou digite `/start`

#### 7.2 Primeiro Teste
```
Você: /start
Bot: 🏥 Bem-vindo ao Médico de Bolso!
      Sou seu assistente médico virtual...
      
Você: /help
Bot: 📋 Comandos disponíveis:
     /start - Iniciar atendimento
     /help - Mostrar esta ajuda
```

### Comandos Disponíveis

| Comando | Descrição | Exemplo |
|---------|-----------|----------|
| `/start` | Iniciar nova consulta médica | `/start` |
| `/help` | Mostrar ajuda e comandos | `/help` |
| `/status` | Verificar status do sistema de IA | `/status` |
| `/reset` | Resetar sistema (em caso de problemas) | `/reset` |
| Texto livre | Descrever sintomas | "Estou com dor de cabeça há 2 dias" |

### Fluxo Completo de Uso

#### 🔄 Exemplo de Consulta Completa

```
👤 Usuário: /start
🤖 Bot: 🏥 Olá! Sou o Médico de Bolso, seu assistente para triagem médica inicial.

⚠️ IMPORTANTE: Não substituo consulta médica profissional.

Como posso ajudá-lo hoje? Descreva seus sintomas.

👤 Usuário: Estou com dor de cabeça forte há 2 dias, febre e enjoo

🤖 Bot: 🩺 Entendi. Vou analisar seus sintomas:

📊 ANÁLISE INICIAL:
• Dor de cabeça persistente (2 dias)
• Febre
• Enjoo/náusea

❓ Para melhor avaliação, preciso de mais informações:

1. Qual a intensidade da dor (1-10)?
2. A febre é alta? Mediu a temperatura?
3. Teve vômitos?
4. Tem rigidez no pescoço?

👤 Usuário: Dor nível 8, febre 39°C, vomitei 2 vezes, pescoço rígido

🤖 Bot: 🚨 ATENÇÃO - SITUAÇÃO DE URGÊNCIA!

Seus sintomas sugerem possível quadro que requer avaliação médica IMEDIATA:

⚠️ RECOMENDAÇÃO:
• Procure PRONTO-SOCORRO agora
• Não aguarde
• Leve alguém com você

📞 Em caso de emergência: 192 (SAMU)

💡 Sintomas que motivam urgência:
• Febre alta + rigidez de pescoço
• Vômitos persistentes
• Dor de cabeça intensa

Este atendimento foi registrado. Cuide-se!
```

### 📱 Dicas de Uso

#### ✅ Como Descrever Sintomas
- **Seja específico**: "Dor no peito esquerdo" em vez de "dor"
- **Inclua duração**: "há 3 dias", "desde ontem"
- **Descreva intensidade**: "dor leve", "dor muito forte"
- **Mencione fatores**: "piora ao respirar", "melhora com repouso"

#### ✅ Informações Úteis
- Idade e sexo
- Medicamentos em uso
- Doenças pré-existentes
- Alergias conhecidas
- Quando começaram os sintomas

#### ❌ O que NÃO fazer
- Não use para emergências reais (chame 192)
- Não substitua consulta médica
- Não tome medicamentos sem orientação
- Não ignore recomendações de procurar ajuda

### 🔧 Solução de Problemas

#### Bot não responde?
1. **Verifique se o bot está rodando**:
   ```bash
   # No terminal onde executou o bot, deve aparecer:
   INFO - Bot iniciado com sucesso
   INFO - Aguardando mensagens...
   ```

2. **Verifique as configurações**:
   ```bash
   # Execute novamente com verificações
   python run.py
   ```

3. **Verifique o token do bot**:
   - Token correto no arquivo `.env`?
   - Bot criado corretamente no @BotFather?

#### Erro de API Gemini?
1. **Verifique a chave da API**:
   - Chave correta no arquivo `.env`?
   - Chave ativa no Google AI Studio?

2. **Verifique conexão com internet**

#### Bot responde com erro?
1. **Verifique os logs**:
   ```bash
   # Veja o arquivo de log
   cat logs/medico_bolso.log
   # ou no Windows
   type logs\medico_bolso.log
   ```

### 🎯 Casos de Uso Recomendados

#### ✅ Ideal para:
- Sintomas leves a moderados
- Dúvidas sobre quando procurar médico
- Orientação inicial sobre sintomas
- Triagem de urgência
- Informações gerais de saúde

#### ⚠️ Procure médico diretamente para:
- Dor no peito
- Falta de ar severa
- Perda de consciência
- Sangramento intenso
- Trauma grave
- Sintomas neurológicos súbitos

## 🏗️ Arquitetura do Projeto

```
medico-de-bolso/
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
├── .env.example           # Exemplo de variáveis de ambiente
├── .gitignore             # Arquivos ignorados pelo Git
└── src/
    ├── __init__.py
    ├── bot/                # Módulos do bot Telegram
    │   ├── __init__.py
    │   └── handlers.py     # Handlers de comandos e mensagens
    ├── ai/                 # Integração com IA
    │   ├── __init__.py
    │   └── gemini_client.py # Cliente Gemini AI
    ├── medical/            # Lógica médica
    │   ├── __init__.py
    │   └── triage.py       # Sistema de triagem
    ├── mcp/                # Model Context Protocol
    │   ├── __init__.py
    │   └── client.py       # Cliente MCP
    ├── config/             # Configurações
    │   ├── __init__.py
    │   └── settings.py     # Configurações do sistema
    └── utils/              # Utilitários
        ├── __init__.py
        ├── logger.py       # Sistema de logging
        └── session_manager.py # Gerenciador de sessões
```

## 🔧 Configuração Avançada

### Configurações de Logging
```env
LOG_LEVEL=INFO              # DEBUG, INFO, WARNING, ERROR
LOG_FILE=medico_bolso.log   # Nome do arquivo de log
```

### Configurações Médicas
```env
MAX_CONSULTATION_LENGTH=2000  # Tamanho máximo da consulta
SESSION_TIMEOUT=1800         # Timeout da sessão (segundos)
```

### Configurações MCP
```env
MCP_SERVER_URL=http://localhost:8080
MCP_API_KEY=sua_chave_mcp
```

## 📊 Funcionalidades

### Sistema de Triagem
- **Detecção de Emergências**: Identifica sintomas que requerem atenção imediata
- **Classificação de Urgência**: Categoriza sintomas por nível de prioridade
- **Fatores de Risco**: Considera idade, condições pré-existentes, etc.
- **Recomendações**: Fornece orientações específicas baseadas na análise

### Integração com Gemini AI
- **Processamento Natural**: Entende linguagem natural em português
- **Contexto Médico**: Especializado em terminologia médica
- **Histórico de Conversa**: Mantém contexto durante a consulta
- **Respostas Personalizadas**: Adapta respostas ao perfil do usuário

### Sistema de Fallback Inteligente
- **Múltiplas APIs**: Suporte para até 5 chaves API do Gemini
- **Múltiplos Modelos**: Rotação entre gemini-1.5-pro, gemini-1.5-flash, gemini-pro, gemini-1.0-pro
- **Detecção Automática**: Identifica rate limits, quotas esgotadas e erros de autenticação
- **Cooldown Inteligente**: Sistema de pausa temporária para APIs com rate limit
- **Recuperação Automática**: Volta a usar APIs após período de cooldown
- **Monitoramento**: Comandos `/status` e `/reset` para administração
- **Alta Disponibilidade**: Garante funcionamento mesmo com falhas em APIs individuais

### Gerenciamento de Sessões
- **Sessões Temporárias**: Controle automático de timeout
- **Histórico de Mensagens**: Mantém contexto da conversa
- **Dados Médicos**: Armazena informações relevantes da consulta
- **Logs de Auditoria**: Registra eventos para análise

## 🔒 Segurança e Privacidade

- **Dados Temporários**: Sessões são removidas automaticamente
- **Logs Seguros**: Informações sensíveis são protegidas
- **Criptografia**: Tokens e chaves são criptografados
- **Compliance**: Segue boas práticas de segurança médica

## ❓ Perguntas Frequentes (FAQ)

### 🔧 Instalação e Configuração

**Q: Erro "python não é reconhecido como comando"**
```bash
# Solução: Instale Python ou use python3
python3 --version
# ou adicione Python ao PATH do sistema
```

**Q: Erro ao instalar dependências**
```bash
# Solução: Atualize pip e tente novamente
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Q: Como obter token do Telegram?**
1. Procure @BotFather no Telegram
2. Digite `/newbot`
3. Siga as instruções
4. Copie o token fornecido

**Q: Onde conseguir chave do Gemini?**
- Acesse: https://makersuite.google.com/app/apikey
- Faça login com conta Google
- Clique "Create API Key"
- Copie a chave gerada

### 🤖 Uso do Bot

**Q: Bot não responde no Telegram**
- Verifique se o bot está rodando no terminal
- Confirme o token no arquivo `.env`
- Teste com `/start`

**Q: Bot responde "Erro interno"**
- Verifique chave Gemini no `.env`
- Confirme conexão com internet
- Veja logs em `logs/medico_bolso.log`

**Q: Como parar o bot?**
```bash
# No terminal onde o bot está rodando:
Ctrl + C  # Windows/Linux
Cmd + C   # Mac
```

**Q: Bot funciona offline?**
- Não, precisa de internet para:
  - Conectar ao Telegram
  - Acessar API do Gemini
  - Funcionalidades MCP

### 🏥 Funcionalidades Médicas

**Q: O bot pode dar diagnósticos?**
- **NÃO!** Apenas triagem inicial
- Sempre recomenda consulta médica
- Identifica situações de urgência

**Q: É seguro usar para emergências?**
- **NÃO!** Para emergências: 192 (SAMU)
- Use apenas para orientação inicial
- Em dúvida, procure pronto-socorro

**Q: Bot armazena dados médicos?**
- Dados temporários apenas durante sessão
- Logs para auditoria (sem dados pessoais)
- Sessões expiram automaticamente

### 💻 Problemas Técnicos

**Q: "ModuleNotFoundError"**
```bash
# Solução: Ative ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

**Q: "Permission denied"**
```bash
# Solução: Execute como administrador ou
# mude permissões da pasta
chmod 755 .  # Linux/Mac
```

**Q: Bot muito lento**
- Verifique conexão com internet
- API Gemini pode ter latência
- Considere usar servidor mais próximo

## 🧪 Testes e Validação

### Testes Automatizados
```bash
# Instalar dependências de teste
pip install pytest pytest-asyncio pytest-cov

# Executar todos os testes
pytest

# Testes com cobertura
pytest --cov=src --cov-report=html

# Testes específicos
pytest tests/test_triage.py -v
pytest tests/test_gemini.py -v
```

### Testes Manuais

#### ✅ Checklist de Funcionamento

**1. Configuração Básica**
- [ ] Ambiente virtual ativado
- [ ] Dependências instaladas
- [ ] Arquivo `.env` configurado
- [ ] Bot criado no Telegram
- [ ] Chave Gemini obtida

**2. Inicialização**
- [ ] `python run.py` executa sem erros
- [ ] Mensagem "Bot iniciado com sucesso"
- [ ] Logs sendo gerados

**3. Funcionalidades Telegram**
- [ ] Bot responde a `/start`
- [ ] Bot responde a `/help`
- [ ] Bot responde a `/status`
- [ ] Bot responde a `/reset`
- [ ] Bot processa mensagens de texto
- [ ] Respostas em português

**4. Funcionalidades Médicas**
- [ ] Detecta sintomas de emergência
- [ ] Classifica urgência corretamente
- [ ] Fornece recomendações apropriadas
- [ ] Mantém contexto da conversa

**5. Sistema de Logs**
- [ ] Arquivo `logs/medico_bolso.log` criado
- [ ] Eventos médicos registrados
- [ ] Erros capturados nos logs

**6. Sistema de Fallback**
- [ ] `/status` mostra APIs configuradas
- [ ] Sistema detecta APIs inválidas
- [ ] Fallback funciona quando API principal falha
- [ ] `/reset` limpa combinações falhadas
- [ ] Cooldown aplicado em rate limits

### 🔍 Comandos de Diagnóstico

```bash
# Verificar status do sistema
python -c "import sys; print(f'Python: {sys.version}')"
python -c "import telegram; print(f'python-telegram-bot: {telegram.__version__}')"
python -c "import google.generativeai; print('Gemini: OK')"

# Testar conectividade
ping google.com
ping api.telegram.org

# Verificar arquivos de configuração
ls -la .env  # Linux/Mac
dir .env     # Windows

# Verificar logs
tail -f logs/medico_bolso.log  # Linux/Mac
type logs\medico_bolso.log     # Windows

# Testar sistema de fallback
python test_fallback.py
```

### 🔄 Testando o Sistema de Fallback

**Script de Teste Automático:**
```bash
python test_fallback.py
```

**Teste Manual via Telegram:**
1. **Verificar Status**: Envie `/status` para ver APIs ativas
2. **Simular Falha**: Modifique temporariamente uma chave API no `.env`
3. **Testar Fallback**: Faça uma consulta médica
4. **Verificar Mudança**: Envie `/status` novamente
5. **Resetar Sistema**: Use `/reset` para limpar falhas

**Exemplo de Saída do `/status`:**
```
🔧 Status do Sistema de IA

📡 API Atual: 2/3
🤖 Modelo Atual: gemini-1.5-pro

✅ Combinações Disponíveis: 8
❌ Combinações Falhadas: 2
⏳ Rate Limited: 1

🟢 Sistema Operacional
```

## 📈 Monitoramento

### Logs Disponíveis
- `logs/medico_bolso.log` - Log geral da aplicação
- `logs/medical_events.log` - Log específico de eventos médicos

### Métricas
- Número de consultas por dia
- Tempo médio de resposta
- Tipos de sintomas mais comuns
- Taxa de emergências detectadas

## 🚀 Deploy em Produção

### 🐳 Docker (Recomendado)

#### Criar Dockerfile
```dockerfile
# Crie um arquivo chamado 'Dockerfile'
FROM python:3.9-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar arquivos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Criar diretórios necessários
RUN mkdir -p logs data cache

# Comando de inicialização
CMD ["python", "main.py"]
```

#### Comandos Docker
```bash
# Build da imagem
docker build -t medico-de-bolso .

# Executar container
docker run -d \
  --name medico-bot \
  --env-file .env \
  --restart unless-stopped \
  -v $(pwd)/logs:/app/logs \
  medico-de-bolso

# Ver logs do container
docker logs -f medico-bot

# Parar container
docker stop medico-bot
```

### 🖥️ Servidor Linux (Ubuntu/Debian)

#### Instalação Completa
```bash
# 1. Atualizar sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar Python e dependências
sudo apt install -y python3 python3-pip python3-venv git

# 3. Criar usuário para o bot
sudo useradd -m -s /bin/bash medicobot
sudo su - medicobot

# 4. Clonar projeto
git clone https://github.com/seu-usuario/medico-de-bolso.git
cd medico-de-bolso

# 5. Configurar ambiente
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 6. Configurar .env
cp .env.example .env
nano .env  # Editar com suas credenciais

# 7. Testar
python run.py
```

#### Criar Serviço Systemd
```bash
# Criar arquivo de serviço
sudo nano /etc/systemd/system/medico-bolso.service
```

```ini
[Unit]
Description=Medico de Bolso Telegram Bot
After=network.target

[Service]
Type=simple
User=medicobot
WorkingDirectory=/home/medicobot/medico-de-bolso
Environment=PATH=/home/medicobot/medico-de-bolso/venv/bin
ExecStart=/home/medicobot/medico-de-bolso/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Ativar e iniciar serviço
sudo systemctl daemon-reload
sudo systemctl enable medico-bolso
sudo systemctl start medico-bolso

# Verificar status
sudo systemctl status medico-bolso

# Ver logs
sudo journalctl -u medico-bolso -f
```

### ☁️ Deploy na Nuvem

#### Heroku
```bash
# 1. Instalar Heroku CLI
# 2. Login
heroku login

# 3. Criar app
heroku create seu-medico-bot

# 4. Configurar variáveis
heroku config:set TELEGRAM_BOT_TOKEN=seu_token
heroku config:set GEMINI_API_KEY=sua_chave

# 5. Deploy
git push heroku main
```

#### Railway
```bash
# 1. Conectar repositório GitHub
# 2. Configurar variáveis de ambiente
# 3. Deploy automático
```

#### VPS/Cloud Server
```bash
# Usar Docker Compose para facilitar
# Criar docker-compose.yml:
version: '3.8'
services:
  medico-bot:
    build: .
    restart: unless-stopped
    env_file: .env
    volumes:
      - ./logs:/app/logs
      - ./data:/app/data

# Executar
docker-compose up -d
```

### 🔧 Monitoramento em Produção

#### Logs e Alertas
```bash
# Configurar logrotate
sudo nano /etc/logrotate.d/medico-bolso
```

```
/home/medicobot/medico-de-bolso/logs/*.log {
    daily
    missingok
    rotate 30
    compress
    delaycompress
    notifempty
    copytruncate
}
```

#### Health Check
```python
# Adicionar endpoint de health check
# health_check.py
import requests
import sys

def check_bot_health():
    try:
        # Verificar se bot responde
        response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getMe")
        if response.status_code == 200:
            print("✅ Bot está funcionando")
            return True
        else:
            print("❌ Bot não responde")
            return False
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False

if __name__ == "__main__":
    if not check_bot_health():
        sys.exit(1)
```

### 📊 Backup e Recuperação

```bash
# Script de backup
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/medico-bolso"

# Criar backup
mkdir -p $BACKUP_DIR
tar -czf $BACKUP_DIR/backup_$DATE.tar.gz \
    /home/medicobot/medico-de-bolso \
    --exclude=venv \
    --exclude=__pycache__ \
    --exclude=*.pyc

# Manter apenas últimos 7 backups
find $BACKUP_DIR -name "backup_*.tar.gz" -mtime +7 -delete

echo "Backup criado: backup_$DATE.tar.gz"
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚠️ Disclaimer Legal

**IMPORTANTE**: Este software é fornecido "como está", sem garantias de qualquer tipo. Os desenvolvedores não se responsabilizam por:

- Diagnósticos incorretos ou imprecisos
- Decisões médicas baseadas nas orientações do bot
- Consequências do uso inadequado do sistema
- Falhas técnicas ou indisponibilidade do serviço

**SEMPRE consulte um profissional de saúde qualificado para questões médicas.**

## 📞 Suporte

- 📧 Email: suporte@medico-de-bolso.com
- 🐛 Issues: [GitHub Issues](https://github.com/seu-usuario/medico-de-bolso/issues)
- 📖 Documentação: [Wiki do Projeto](https://github.com/seu-usuario/medico-de-bolso/wiki)

## 🙏 Agradecimentos

- Google Gemini AI pela tecnologia de IA
- Telegram pela plataforma de bot
- Comunidade Python pelo ecossistema
- Profissionais de saúde pelas orientações médicas

## 🚀 Resumo Rápido - Como Começar

### ⚡ Início Rápido (5 minutos)

```bash
# 1. Baixar projeto
git clone https://github.com/seu-usuario/medico-de-bolso.git
cd medico-de-bolso

# 2. Configurar ambiente
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Configurar credenciais
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac
# Editar .env com suas credenciais

# 5. Executar
python run.py
```

### 📋 Checklist Essencial

- [ ] **Python 3.8+** instalado
- [ ] **Token Telegram** obtido via @BotFather
- [ ] **Chave Gemini** obtida em https://makersuite.google.com/app/apikey
- [ ] **Arquivo .env** configurado corretamente
- [ ] **Dependências** instaladas com `pip install -r requirements.txt`
- [ ] **Bot testado** com `/start` no Telegram

### 🆘 Links Importantes

| Recurso | Link |
|---------|------|
| 🤖 Criar Bot Telegram | @BotFather no Telegram |
| 🧠 API Gemini | https://makersuite.google.com/app/apikey |
| 📚 Documentação Python | https://python.org |
| 🐛 Reportar Problemas | [GitHub Issues](https://github.com/seu-usuario/medico-de-bolso/issues) |
| 💬 Suporte | suporte@medico-de-bolso.com |

### ⚠️ Lembretes Importantes

- 🚨 **NUNCA** use para emergências reais - chame 192 (SAMU)
- 🔒 **NÃO** compartilhe seu arquivo `.env`
- 🏥 **SEMPRE** recomende consulta médica profissional
- 📱 Bot funciona apenas **COM INTERNET**
- 🔄 Mantenha o **terminal aberto** enquanto o bot estiver rodando

### 🎯 Próximos Passos

1. **Teste básico**: Envie `/start` para seu bot
2. **Teste médico**: Descreva sintomas simples
3. **Verifique logs**: Confira arquivo `logs/medico_bolso.log`
4. **Personalize**: Ajuste configurações no `.env`
5. **Deploy**: Use Docker ou servidor para produção

---

**Desenvolvido com ❤️ para ajudar na triagem médica inicial**

*"A tecnologia a serviço da saúde, sempre com responsabilidade e ética."*
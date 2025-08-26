
**🏥 Mangaba AI - Transformando o atendimento médico com IA** 🤖

*Desenvolvido com ❤️ para democratizar o acesso à orientação médica*

[![GitHub](https://img.shields.io/badge/GitHub-mangaba--telegram-blue?style=for-the-badge&logo=github)](https://github.com/seu-usuario/mangaba-telegram)
[![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)](https://telegram.org)

</div>

### 🏗️ Componentes Principais

| Componente | Descrição | Tecnologia |
|------------|-----------|------------|
| **MangabaAICore** | Sistema integrado híbrido | MCP + A2A |
| **ConversationAgents** | Agentes colaborativos | A2A Pattern |
| **GeminiClient** | Interface IA médica | Google Gemini |
| **MCPClient** | Recursos médicos externos | Model Context Protocol |
| **MedicalTriage** | Sistema de triagem | Algoritmos médicos |
| **SessionManager** | Gerenciamento de estado | Redis/SQLite |

## 📋 Pré-requisitos

### 🐍 **Ambiente de Desenvolvimento**
- **Python**: 3.8 ou superior
- **Sistema Operacional**: Windows, Linux ou macOS
- **Memória RAM**: Mínimo 2GB (recomendado 4GB)
- **Espaço em Disco**: 500MB livres

### 🔑 **Credenciais Necessárias**
- **Token do Bot Telegram**: Obtido via [@BotFather](https://t.me/BotFather)
- **Chave da API Google Gemini**: [Google AI Studio](https://makersuite.google.com/app/apikey)
- **Conexão com Internet**: Para comunicação com APIs

### 📦 **Dependências Principais**
- `python-telegram-bot`: Interface Telegram
- `google-generativeai`: IA Gemini
- `aiohttp`: Cliente HTTP assíncrono
- `loguru`: Sistema de logs avançado
- `pydantic`: Validação de dados

## 🚀 Instalação Rápida

### 📥 **Método 1: Clone do Repositório (Recomendado)**

```bash
# 1. Clonar o repositório
git clone https://github.com/seu-usuario/mangaba-telegram.git
cd mangaba-telegram

# 2. Verificar Python (3.8+)
python --version

# 3. Criar ambiente virtual
python -m venv venv

# 4. Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 5. Instalar dependências
pip install --upgrade pip
pip install -r requirements.txt

# 6. Configurar variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# 7. Executar o bot
python main.py
```

### 📦 **Método 2: Download Direto**

1. **Baixe o ZIP** do [repositório GitHub](https://github.com/seu-usuario/mangaba-telegram)
2. **Extraia** em uma pasta de sua escolha
3. **Abra o terminal** na pasta extraída
4. **Siga os passos 2-7** do método anterior

---

## 🛠️ Instalação Detalhada

<details>
<summary>📖 <strong>Clique para ver instruções detalhadas</strong></summary>

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
git clone https://github.com/seu-usuario/mangaba-telegram.git
cd mangaba-telegram

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

#### 3.3 Verificar Instalação
```bash
# Verificar se as principais dependências foram instaladas
python -c "import telegram, google.generativeai, aiohttp; print('✅ Dependências instaladas com sucesso!')"
```

</details>

## 🔑 Configuração de Credenciais

### 🤖 **Passo 1: Criar Bot no Telegram**

1. **Abra o Telegram** e procure por [@BotFather](https://t.me/BotFather)
2. **Inicie conversa** com `/start`
3. **Crie novo bot** com `/newbot`
4. **Escolha um nome** para seu bot (ex: "Mangaba AI Médico")
5. **Escolha um username** único (ex: "mangaba_ai_medico_bot")
6. **Copie o token** que aparece

```
Formato do token: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

### 🧠 **Passo 2: Obter Chave do Google Gemini**

1. **Acesse**: [Google AI Studio](https://makersuite.google.com/app/apikey)
2. **Faça login** com sua conta Google
3. **Clique em "Create API Key"**
4. **Copie a chave** gerada

```
Formato da chave: AIzaSyC...
```

### 🔄 **Passo 3: Sistema de Fallback (Opcional)**

Para alta disponibilidade, recomendamos configurar múltiplas chaves API:

- **Crie 2-5 projetos** diferentes no Google AI Studio
- **Gere uma chave** para cada projeto
- **Configure no arquivo `.env`** (veja próxima seção)

## ⚙️ Configuração do Sistema

### 📝 **Configurar Variáveis de Ambiente**

#### 1. Copiar arquivo de exemplo
```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

#### 2. Editar configurações

Abra o arquivo `.env` e configure suas credenciais:

```env
# ========== 🔑 CREDENCIAIS OBRIGATÓRIAS ==========
TELEGRAM_BOT_TOKEN=seu_token_telegram_aqui
GEMINI_API_KEY=sua_chave_gemini_aqui

# ========== 🔄 SISTEMA DE FALLBACK (RECOMENDADO) ==========
GEMINI_API_KEY_2=sua_segunda_chave_aqui
GEMINI_API_KEY_3=sua_terceira_chave_aqui
GEMINI_API_KEY_4=sua_quarta_chave_aqui
GEMINI_API_KEY_5=sua_quinta_chave_aqui

# ========== ⚙️ CONFIGURAÇÕES OPCIONAIS ==========
LOG_LEVEL=INFO
SESSION_TIMEOUT=1800
MAX_CONSULTATION_LENGTH=2000
```

### 🔄 **Sistema de Fallback**

<div align="center">
<table>
<tr>
<td align="center">

**🚀 Alta Disponibilidade**

Configurar múltiplas chaves API garante:
- ✅ **99.9% de uptime**
- ✅ **Distribuição de carga**
- ✅ **Recuperação automática**
- ✅ **Proteção contra rate limits**

</td>
</tr>
</table>
</div>

### 🔒 **Segurança**

> **⚠️ IMPORTANTE**: Nunca compartilhe seu arquivo `.env` ou commit ele no Git. Ele contém informações sensíveis!

**⚙️ Como funciona:**
- O bot usa `GEMINI_API_KEY` como principal
- Se falhar, tenta `GEMINI_API_KEY_2`, depois `GEMINI_API_KEY_3`, etc.
- Detecta automaticamente rate limits e quotas esgotadas
- Aplica cooldown temporário em APIs com problemas
- Use `/status` para monitorar o sistema
- Use `/reset` para resetar falhas temporárias





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



---

**Desenvolvido com ❤️ para ajudar na triagem médica inicial**

*"A tecnologia a serviço da saúde, sempre com responsabilidade e ética."*

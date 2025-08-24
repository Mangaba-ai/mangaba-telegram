# 🤖 Mangaba AI - Sistema de IA Médica Avançado

## 🚀 Alias de Marketing

O **Mangaba AI** é o nome de marketing para o sistema "Médico de Bolso". Agora você pode importar e usar todos os componentes com o alias `mangaba_ai` para uma experiência mais profissional e comercial.

## 📦 Instalação e Uso

### Importação Direta
```python
# Importar componentes específicos
from src import GeminiMedicalAI, ConversationManager, QuickResponseEngine
from src import MedicalTriage, SessionManager, setup_logger

# Usar os componentes
ai_client = GeminiMedicalAI()
conversation = ConversationManager()
```

### Importação com Alias Mangaba AI
```python
# Importar como mangaba_ai
import src as mangaba_ai

# Usar com o alias de marketing
ai_medico = mangaba_ai.GeminiMedicalAI()
conversa = mangaba_ai.ConversationManager()
triagem = mangaba_ai.MedicalTriage()

# Informações do sistema
print(f"Versão: {mangaba_ai.__version__}")
print(f"Autor: {mangaba_ai.__author__}")
print(f"Descrição: {mangaba_ai.__description__}")
```

## 🎯 Componentes Disponíveis

### 🤖 IA e Conversação
- `mangaba_ai.GeminiMedicalAI` - Cliente de IA médica principal
- `mangaba_ai.ConversationManager` - Gerenciador de conversação dinâmica
- `mangaba_ai.QuickResponseEngine` - Sistema de respostas rápidas

### 🩺 Sistema Médico
- `mangaba_ai.MedicalTriage` - Sistema de triagem médica
- `mangaba_ai.SessionManager` - Gerenciador de sessões

### 🔧 Utilitários
- `mangaba_ai.setup_logger` - Configuração de logging

### 🤖 Handlers do Bot
- `mangaba_ai.start_handler` - Handler de início
- `mangaba_ai.help_handler` - Handler de ajuda
- `mangaba_ai.medical_consultation_handler` - Handler de consulta médica
- `mangaba_ai.status_handler` - Handler de status
- `mangaba_ai.reset_handler` - Handler de reset

## 🌟 Exemplo Completo

```python
#!/usr/bin/env python3
import src as mangaba_ai

def inicializar_sistema_medico():
    """Inicializa o sistema Mangaba AI completo"""
    
    # Configurar logging
    mangaba_ai.setup_logger()
    
    # Inicializar componentes principais
    ai_client = mangaba_ai.GeminiMedicalAI()
    conversation_manager = mangaba_ai.ConversationManager()
    triage_system = mangaba_ai.MedicalTriage()
    session_manager = mangaba_ai.SessionManager()
    
    print(f"🤖 {mangaba_ai.__description__}")
    print(f"📋 Versão: {mangaba_ai.__version__}")
    print(f"✅ Sistema inicializado com sucesso!")
    
    return {
        'ai': ai_client,
        'conversation': conversation_manager,
        'triage': triage_system,
        'session': session_manager
    }

if __name__ == "__main__":
    sistema = inicializar_sistema_medico()
    print("🎉 Mangaba AI pronto para uso!")
```

## 🔍 Informações do Sistema

- **Versão**: 1.0.0
- **Autor**: Mangaba AI Team
- **Descrição**: Sistema de IA Médica Avançado para Telegram

## 🚀 Capacidades

### 🤖 Agentes de IA A2A
- Sistema de agentes colaborativos
- Conversação dinâmica e natural
- Adaptação inteligente ao contexto

### ⚡ Respostas Rápidas
- Reconhecimento automático de padrões
- Respostas instantâneas para consultas comuns
- Redução significativa no tempo de resposta

### 🩺 Sistema Médico Avançado
- Triagem médica inteligente
- Detecção automática de emergências
- Análise de sintomas contextual

### 💬 Conversação Inteligente
- Múltiplos modos de conversação
- Consciência de contexto
- Follow-up automático

## 📈 Benefícios do Alias Mangaba AI

1. **Branding Profissional**: Nome comercial mais atrativo
2. **Facilidade de Uso**: Importação simplificada
3. **Compatibilidade**: Não afeta o funcionamento existente
4. **Marketing**: Melhor apresentação para clientes
5. **Escalabilidade**: Preparado para expansão comercial

## 🔧 Compatibilidade

✅ **Totalmente compatível** com o código existente
✅ **Não afeta** o funcionamento atual do bot
✅ **Mantém** todas as funcionalidades
✅ **Adiciona** apenas o alias de marketing

---

**Mangaba AI** - Transformando o atendimento médico com inteligência artificial avançada! 🩺🤖
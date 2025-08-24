#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Logging - Médico de Bolso
Configura e gerencia logs do sistema
"""

import logging
import logging.handlers
import os
from datetime import datetime
from src.config.settings import LOG_LEVEL, LOG_FILE

def setup_logger():
    """Configura o sistema de logging"""
    # Criar diretório de logs se não existir
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Configurar formato dos logs
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configurar logger raiz
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, LOG_LEVEL.upper()))
    
    # Limpar handlers existentes
    root_logger.handlers.clear()
    
    # Handler para arquivo com rotação
    file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(log_dir, LOG_FILE),
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    
    # Handler para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    console_handler.setLevel(getattr(logging, LOG_LEVEL.upper()))
    
    # Adicionar handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Log inicial
    logger = logging.getLogger(__name__)
    logger.info("Sistema de logging inicializado")
    logger.info(f"Nível de log: {LOG_LEVEL}")
    logger.info(f"Arquivo de log: {os.path.join(log_dir, LOG_FILE)}")

def get_logger(name: str) -> logging.Logger:
    """Retorna um logger configurado para o módulo especificado"""
    return logging.getLogger(name)

class MedicalLogger:
    """Logger especializado para eventos médicos"""
    
    def __init__(self):
        self.logger = logging.getLogger('medical_events')
        
        # Criar handler específico para eventos médicos
        medical_handler = logging.FileHandler(
            os.path.join('logs', 'medical_events.log'),
            encoding='utf-8'
        )
        
        medical_format = logging.Formatter(
            '%(asctime)s - MEDICAL - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        medical_handler.setFormatter(medical_format)
        
        self.logger.addHandler(medical_handler)
        self.logger.setLevel(logging.INFO)
    
    def log_consultation(self, user_id: int, symptoms: str, urgency: str):
        """Log de consulta médica"""
        self.logger.info(
            f"CONSULTA - User: {user_id} | Urgência: {urgency} | Sintomas: {symptoms[:100]}..."
        )
    
    def log_emergency(self, user_id: int, symptoms: str):
        """Log de emergência detectada"""
        self.logger.warning(
            f"EMERGÊNCIA - User: {user_id} | Sintomas: {symptoms[:100]}..."
        )
    
    def log_session_start(self, user_id: int, user_name: str):
        """Log de início de sessão"""
        self.logger.info(
            f"SESSÃO_INICIADA - User: {user_id} | Nome: {user_name}"
        )
    
    def log_session_end(self, user_id: int, duration_minutes: int):
        """Log de fim de sessão"""
        self.logger.info(
            f"SESSÃO_FINALIZADA - User: {user_id} | Duração: {duration_minutes}min"
        )

# Instância global do logger médico
medical_logger = MedicalLogger()
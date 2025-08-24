#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cliente MCP - Médico de Bolso
Model Context Protocol para comunicação avançada
"""

import asyncio
import json
import logging
import aiohttp
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from src.config.settings import MCP_SERVER_URL, MCP_API_KEY

logger = logging.getLogger(__name__)

@dataclass
class MCPMessage:
    """Mensagem do protocolo MCP"""
    method: str
    params: Dict[str, Any]
    id: Optional[str] = None
    jsonrpc: str = "2.0"

@dataclass
class MCPResponse:
    """Resposta do protocolo MCP"""
    result: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, Any]] = None
    id: Optional[str] = None
    jsonrpc: str = "2.0"

class MCPClient:
    """Cliente para comunicação via Model Context Protocol"""
    
    def __init__(self):
        """Inicializa o cliente MCP"""
        self.server_url = MCP_SERVER_URL
        self.api_key = MCP_API_KEY
        self.session = None
        self.connected = False
        logger.info("Cliente MCP inicializado")
    
    async def connect(self) -> bool:
        """Conecta ao servidor MCP"""
        try:
            self.session = aiohttp.ClientSession(
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}' if self.api_key else None
                },
                timeout=aiohttp.ClientTimeout(total=30)
            )
            
            # Testar conexão
            response = await self._send_message(MCPMessage(
                method="initialize",
                params={
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "roots": {"listChanged": True},
                        "sampling": {}
                    },
                    "clientInfo": {
                        "name": "medico-bolso",
                        "version": "1.0.0"
                    }
                }
            ))
            
            if response and not response.error:
                self.connected = True
                logger.info("Conectado ao servidor MCP com sucesso")
                return True
            else:
                logger.error(f"Erro ao conectar MCP: {response.error if response else 'Sem resposta'}")
                return False
                
        except Exception as e:
            logger.error(f"Erro ao conectar ao servidor MCP: {e}")
            return False
    
    async def disconnect(self):
        """Desconecta do servidor MCP"""
        if self.session:
            await self.session.close()
            self.session = None
        self.connected = False
        logger.info("Desconectado do servidor MCP")
    
    async def get_medical_resources(self, query: str) -> List[Dict[str, Any]]:
        """Busca recursos médicos via MCP"""
        if not self.connected:
            await self.connect()
        
        try:
            response = await self._send_message(MCPMessage(
                method="resources/list",
                params={
                    "query": query,
                    "type": "medical"
                }
            ))
            
            if response and response.result:
                return response.result.get('resources', [])
            else:
                logger.warning(f"Nenhum recurso médico encontrado para: {query}")
                return []
                
        except Exception as e:
            logger.error(f"Erro ao buscar recursos médicos: {e}")
            return []
    
    async def get_drug_interactions(self, medications: List[str]) -> Dict[str, Any]:
        """Verifica interações medicamentosas via MCP"""
        if not self.connected:
            await self.connect()
        
        try:
            response = await self._send_message(MCPMessage(
                method="tools/call",
                params={
                    "name": "check_drug_interactions",
                    "arguments": {
                        "medications": medications
                    }
                }
            ))
            
            if response and response.result:
                return response.result
            else:
                logger.warning(f"Erro ao verificar interações: {response.error if response else 'Sem resposta'}")
                return {}
                
        except Exception as e:
            logger.error(f"Erro ao verificar interações medicamentosas: {e}")
            return {}
    
    async def get_medical_guidelines(self, condition: str) -> Dict[str, Any]:
        """Busca diretrizes médicas para uma condição"""
        if not self.connected:
            await self.connect()
        
        try:
            response = await self._send_message(MCPMessage(
                method="tools/call",
                params={
                    "name": "get_medical_guidelines",
                    "arguments": {
                        "condition": condition,
                        "language": "pt-BR"
                    }
                }
            ))
            
            if response and response.result:
                return response.result
            else:
                return {}
                
        except Exception as e:
            logger.error(f"Erro ao buscar diretrizes médicas: {e}")
            return {}
    
    async def log_medical_event(self, event_data: Dict[str, Any]) -> bool:
        """Registra evento médico via MCP"""
        if not self.connected:
            await self.connect()
        
        try:
            response = await self._send_message(MCPMessage(
                method="notifications/medical_event",
                params=event_data
            ))
            
            return response is not None and not response.error
            
        except Exception as e:
            logger.error(f"Erro ao registrar evento médico: {e}")
            return False
    
    async def get_emergency_protocols(self, symptoms: List[str]) -> Dict[str, Any]:
        """Busca protocolos de emergência baseados em sintomas"""
        if not self.connected:
            await self.connect()
        
        try:
            response = await self._send_message(MCPMessage(
                method="tools/call",
                params={
                    "name": "emergency_protocols",
                    "arguments": {
                        "symptoms": symptoms,
                        "language": "pt-BR"
                    }
                }
            ))
            
            if response and response.result:
                return response.result
            else:
                return {}
                
        except Exception as e:
            logger.error(f"Erro ao buscar protocolos de emergência: {e}")
            return {}
    
    async def _send_message(self, message: MCPMessage) -> Optional[MCPResponse]:
        """Envia mensagem para o servidor MCP"""
        if not self.session:
            return None
        
        try:
            payload = {
                "jsonrpc": message.jsonrpc,
                "method": message.method,
                "params": message.params
            }
            
            if message.id:
                payload["id"] = message.id
            
            async with self.session.post(
                f"{self.server_url}/mcp",
                json=payload
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return MCPResponse(
                        result=data.get('result'),
                        error=data.get('error'),
                        id=data.get('id'),
                        jsonrpc=data.get('jsonrpc', '2.0')
                    )
                else:
                    logger.error(f"Erro HTTP {response.status} ao enviar mensagem MCP")
                    return None
                    
        except Exception as e:
            logger.error(f"Erro ao enviar mensagem MCP: {e}")
            return None
    
    async def __aenter__(self):
        """Context manager entry"""
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        await self.disconnect()

# Instância global do cliente MCP
mcp_client = MCPClient()
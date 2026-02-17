"""
Multi-provider AI client for Garmin Chat Desktop.
Supports: xAI (Grok), OpenAI (ChatGPT), Azure OpenAI, Google Gemini, Anthropic (Claude), Ollama
"""

from openai import OpenAI, AzureOpenAI
from typing import List, Dict, Optional
import logging
import os
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AIClient:
    """Unified AI client that supports multiple providers."""
    
    # Provider configurations
    PROVIDERS = {
        'xai': {
            'name': 'xAI (Grok)',
            'base_url': 'https://api.x.ai/v1',
            'models': ['grok-3', 'grok-vision-beta', 'grok-2-vision-1212'],
            'default_model': 'grok-3',
            'supports_streaming': True
        },
        'openai': {
            'name': 'OpenAI (ChatGPT)',
            'base_url': 'https://api.openai.com/v1',
            'models': ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'gpt-3.5-turbo'],
            'default_model': 'gpt-4o',
            'supports_streaming': True
        },
        'azure': {
            'name': 'Azure OpenAI',
            'base_url': None,  # Set by user
            'models': [],  # Deployment names set by user
            'default_model': None,
            'supports_streaming': True,
            'requires_deployment': True
        },
        'gemini': {
            'name': 'Google Gemini',
            'base_url': 'https://generativelanguage.googleapis.com/v1beta',
            'models': ['gemini-1.5-flash', 'gemini-1.5-flash-8b', 'gemini-1.5-pro'],
            'default_model': 'gemini-1.5-flash',
            'supports_streaming': True,
            'uses_native_sdk': True,  # Use native Google SDK (google-genai package)
            'note': 'Requires google-genai package (replaces deprecated google-generativeai)'
        },
        'anthropic': {
            'name': 'Anthropic (Claude)',
            'base_url': 'https://api.anthropic.com/v1',
            'models': ['claude-opus-4-5-20251101', 'claude-sonnet-4-5-20250929', 'claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022'],
            'default_model': 'claude-sonnet-4-5-20250929',
            'supports_streaming': True,
            'uses_anthropic_sdk': True
        },
        'ollama': {
            'name': 'Ollama (Local)',
            'base_url': 'http://localhost:11434/v1',  # Default Ollama endpoint
            'models': [],  # Dynamically loaded from Ollama server
            'default_model': 'llama2',  # Common default
            'supports_streaming': True,
            'is_local': True,
            'no_api_key': True,
            'note': 'Requires Ollama to be installed and running locally'
        }
    }
    
    def __init__(self, provider: str = 'xai', api_key: str = '', model: str = None, **kwargs):
        """
        Initialize AI client with specified provider.
        
        Args:
            provider: One of 'xai', 'openai', 'azure', 'gemini', 'anthropic', 'ollama'
            api_key: API key for the provider (not needed for Ollama)
            model: Specific model to use (uses default if not specified)
            **kwargs: Additional provider-specific parameters
                - azure_endpoint: Azure OpenAI endpoint URL
                - azure_deployment: Azure deployment name
                - azure_api_version: Azure API version (default: 2024-02-15-preview)
                - ollama_endpoint: Ollama server endpoint (default: http://localhost:11434)
        """
        self.provider = provider
        self.api_key = api_key
        self.conversation_history: List[Dict[str, str]] = []
        
        # Ollama-specific settings
        self.ollama_endpoint = kwargs.get('ollama_endpoint', 'http://localhost:11434')
        
        if provider not in self.PROVIDERS:
            raise ValueError(f"Unsupported provider: {provider}. Choose from: {list(self.PROVIDERS.keys())}")
        
        provider_config = self.PROVIDERS[provider]
        
        # Set model (use default if not specified)
        if model:
            self.model = model
        else:
            self.model = provider_config['default_model']
        
        # Initialize provider-specific client
        if provider == 'xai':
            self.client = self._init_xai()
        elif provider == 'openai':
            self.client = self._init_openai()
        elif provider == 'azure':
            self.client = self._init_azure(kwargs)
        elif provider == 'gemini':
            self.client = self._init_gemini()
        elif provider == 'anthropic':
            self.client = self._init_anthropic()
        elif provider == 'ollama':
            self.client = self._init_ollama()
        
        logger.info(f"Initialized {provider_config['name']} with model: {self.model}")
    
    def _init_xai(self) -> OpenAI:
        """Initialize xAI (Grok) client."""
        return OpenAI(
            api_key=self.api_key,
            base_url=self.PROVIDERS['xai']['base_url']
        )
    
    def _init_openai(self) -> OpenAI:
        """Initialize OpenAI client."""
        return OpenAI(api_key=self.api_key)
    
    def _init_azure(self, kwargs: dict) -> AzureOpenAI:
        """Initialize Azure OpenAI client."""
        azure_endpoint = kwargs.get('azure_endpoint')
        azure_api_version = kwargs.get('azure_api_version', '2024-02-15-preview')
        
        if not azure_endpoint:
            raise ValueError("Azure endpoint is required for Azure OpenAI")
        
        # Store deployment name for Azure
        self.azure_deployment = kwargs.get('azure_deployment', self.model)
        
        return AzureOpenAI(
            api_key=self.api_key,
            azure_endpoint=azure_endpoint,
            api_version=azure_api_version
        )
    
    def _init_gemini(self):
        """Initialize Google Gemini client using new google-genai SDK."""
        try:
            from google import genai
            from google.genai.types import GenerateContentConfig
            
            # Initialize client with API key
            client = genai.Client(api_key=self.api_key)
            
            # Store config for later use
            self.gemini_config = GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=2048,
            )
            
            logger.info("Using new google-genai SDK for Gemini")
            return client
            
        except ImportError:
            logger.error("google-genai package not found. Install with: pip install google-genai")
            raise ImportError(
                "Please install google-genai package: pip install google-genai\n"
                "Note: The old google-generativeai package is deprecated."
            )
    
    def _init_anthropic(self):
        """Initialize Anthropic (Claude) client."""
        try:
            from anthropic import Anthropic
            return Anthropic(api_key=self.api_key)
        except ImportError:
            logger.error("anthropic package not found. Install with: pip install anthropic")
            raise ImportError("Please install anthropic package: pip install anthropic")
    
    def _init_ollama(self) -> OpenAI:
        """Initialize Ollama client (uses OpenAI-compatible API)."""
        logger.info(f"Connecting to Ollama at {self.ollama_endpoint}")
        return OpenAI(
            base_url=f"{self.ollama_endpoint}/v1",
            api_key="ollama"  # Ollama doesn't need a real API key
        )
    
    def chat(self, message: str, context: str = "") -> str:
        """
        Send a chat message and get a response.
        
        Args:
            message: The user's message
            context: Optional context (e.g., Garmin data) to include
            
        Returns:
            The AI's response as a string
        """
        try:
            if self.provider in ['xai', 'openai', 'ollama']:
                return self._chat_openai_style(message, context)
            elif self.provider == 'azure':
                return self._chat_azure(message, context)
            elif self.provider == 'gemini':
                return self._chat_gemini(message, context)
            elif self.provider == 'anthropic':
                return self._chat_anthropic(message, context)
        except Exception as e:
            logger.error(f"Error in chat: {e}")
            if self.provider == 'ollama':
                return (f"Error connecting to Ollama: {e}\n\n"
                       f"Make sure Ollama is installed and running.\n"
                       f"You can start it with: ollama serve")
            return f"Error: {e}"
    
    def _chat_openai_style(self, message: str, context: str) -> str:
        """Handle chat for OpenAI-style APIs (xAI, OpenAI, Ollama)."""
        messages = []
        
        # System message with context
        system_content = "You are a helpful fitness assistant analyzing Garmin Connect data. "
        system_content += "Provide insights, answer questions, and help users understand their fitness metrics."
        
        if context:
            system_content += f"\n\nHere is the user's Garmin data:\n{context}"
        
        messages.append({"role": "system", "content": system_content})
        
        # Add conversation history
        messages.extend(self.conversation_history[-10:])  # Last 10 messages
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Make API call
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.7,
            max_tokens=2048
        )
        
        assistant_message = response.choices[0].message.content
        
        # Update conversation history
        self.conversation_history.append({"role": "user", "content": message})
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def _chat_azure(self, message: str, context: str) -> str:
        """Handle chat for Azure OpenAI."""
        messages = []
        
        # System message with context
        system_content = "You are a helpful fitness assistant analyzing Garmin Connect data. "
        system_content += "Provide insights, answer questions, and help users understand their fitness metrics."
        
        if context:
            system_content += f"\n\nHere is the user's Garmin data:\n{context}"
        
        messages.append({"role": "system", "content": system_content})
        
        # Add conversation history
        messages.extend(self.conversation_history[-10:])
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Make API call (use deployment name for Azure)
        response = self.client.chat.completions.create(
            model=self.azure_deployment,
            messages=messages,
            temperature=0.7,
            max_tokens=2048
        )
        
        assistant_message = response.choices[0].message.content
        
        # Update conversation history
        self.conversation_history.append({"role": "user", "content": message})
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def _chat_gemini(self, message: str, context: str) -> str:
        """Handle chat for Google Gemini using new SDK."""
        try:
            from google.genai.types import GenerateContentConfig
            
            # Build full prompt with context
            full_prompt = message
            if context:
                full_prompt = f"Here is the user's Garmin data:\n{context}\n\nUser question: {message}"
            
            # Build message history for Gemini
            contents = []
            for msg in self.conversation_history[-10:]:
                role = "user" if msg["role"] == "user" else "model"
                contents.append({
                    "role": role,
                    "parts": [{"text": msg["content"]}]
                })
            
            # Add current message
            contents.append({
                "role": "user",
                "parts": [{"text": full_prompt}]
            })
            
            # Make API call
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
                config=self.gemini_config
            )
            
            assistant_message = response.text
            
            # Update conversation history
            self.conversation_history.append({"role": "user", "content": message})
            self.conversation_history.append({"role": "assistant", "content": assistant_message})
            
            return assistant_message
            
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            raise
    
    def _chat_anthropic(self, message: str, context: str) -> str:
        """Handle chat for Anthropic Claude."""
        messages = []
        
        # Add conversation history
        messages.extend(self.conversation_history[-10:])
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Build system message with context
        system_content = "You are a helpful fitness assistant analyzing Garmin Connect data. "
        system_content += "Provide insights, answer questions, and help users understand their fitness metrics."
        
        if context:
            system_content += f"\n\nHere is the user's Garmin data:\n{context}"
        
        # Make API call
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=system_content,
            messages=messages
        )
        
        assistant_message = response.content[0].text
        
        # Update conversation history
        self.conversation_history.append({"role": "user", "content": message})
        self.conversation_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
        logger.info("Conversation history cleared")
    
    @staticmethod
    def get_available_providers() -> Dict[str, dict]:
        """Get dictionary of available AI providers and their configurations."""
        return AIClient.PROVIDERS.copy()
    
    @staticmethod
    def test_ollama_connection(endpoint: str = 'http://localhost:11434') -> Dict[str, any]:
        """
        Test connection to Ollama server and get available models.
        
        Args:
            endpoint: Ollama server endpoint
            
        Returns:
            Dictionary with 'success' (bool), 'message' (str), and optionally 'models' (list)
        """
        try:
            response = requests.get(f"{endpoint}/api/tags", timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                models = [model['name'] for model in data.get('models', [])]
                
                if models:
                    return {
                        'success': True,
                        'models': models,
                        'message': f"Connected successfully. Found {len(models)} model(s)."
                    }
                else:
                    return {
                        'success': True,
                        'models': [],
                        'message': "Connected but no models found. Pull a model with: ollama pull llama2"
                    }
            else:
                return {
                    'success': False,
                    'message': f"Server responded with status {response.status_code}"
                }
                
        except requests.exceptions.ConnectionError:
            return {
                'success': False,
                'message': "Cannot connect to Ollama. Make sure Ollama is installed and running.\nStart with: ollama serve"
            }
        except Exception as e:
            return {
                'success': False,
                'message': f"Error: {str(e)}"
            }
    
    @staticmethod
    def get_ollama_models(endpoint: str = 'http://localhost:11434') -> List[str]:
        """
        Get list of available Ollama models.
        
        Args:
            endpoint: Ollama server endpoint
            
        Returns:
            List of model names
        """
        result = AIClient.test_ollama_connection(endpoint)
        return result.get('models', [])


if __name__ == "__main__":
    # Test basic functionality
    print("AI Client - Provider Support Test")
    print("=" * 50)
    
    providers = AIClient.get_available_providers()
    print(f"\nSupported providers: {len(providers)}")
    for provider_id, config in providers.items():
        print(f"\n{config['name']} ({provider_id}):")
        print(f"  Default model: {config.get('default_model', 'N/A')}")
        if config.get('is_local'):
            print(f"  Type: Local (no API key needed)")
        if config.get('models'):
            print(f"  Available models: {', '.join(config['models'][:3])}...")
    
    # Test Ollama connection if requested
    import sys
    if '--test-ollama' in sys.argv:
        print("\n" + "=" * 50)
        print("Testing Ollama connection...")
        result = AIClient.test_ollama_connection()
        print(f"Success: {result['success']}")
        print(f"Message: {result['message']}")
        if result.get('models'):
            print(f"Models: {', '.join(result['models'])}")

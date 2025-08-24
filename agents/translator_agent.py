"""
Translator Agent - A sample Eidolon AI agent for translation tasks
"""

from eidolon_ai_sdk import Agent, AgentState
from typing import Dict, Any


class TranslatorAgent(Agent):
    """
    An AI agent that can translate text between languages
    """
    
    def __init__(self, **kwargs):
        super().__init__(
            name="translator_agent",
            description="Translates text between different languages",
            system_prompt="""
            You are a helpful translation assistant. 
            When given text, first repeat the original text, 
            then provide an accurate translation to the requested language.
            If no target language is specified, translate to Spanish.
            """,
            **kwargs
        )
    
    async def translate_text(self, text: str, target_language: str = "Spanish") -> Dict[str, Any]:
        """
        Translate text to the target language
        
        Args:
            text: The text to translate
            target_language: The target language for translation
            
        Returns:
            Dictionary containing original text and translation
        """
        prompt = f"Translate the following text to {target_language}: {text}"
        
        response = await self.llm_call(prompt)
        
        return {
            "original_text": text,
            "target_language": target_language,
            "translation": response,
            "agent": self.name
        }
    
    async def detect_and_translate(self, text: str) -> Dict[str, Any]:
        """
        Detect language and translate to English if not already English
        """
        prompt = f"Detect the language of this text and translate to English if needed: {text}"
        
        response = await self.llm_call(prompt)
        
        return {
            "original_text": text,
            "result": response,
            "agent": self.name
        }
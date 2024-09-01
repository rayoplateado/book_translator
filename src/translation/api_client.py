from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from dotenv import load_dotenv
from src.translation.character_context import CharacterContextManager

import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class AnthropicClient:
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.character_context = CharacterContextManager()
    def translate(self, text, target_language, context=""):
        character_info = self.character_context.generate_context_string()
        prompt = f"{HUMAN_PROMPT}Translate the following text to {target_language}. "
        prompt += f"Consider this context about the characters:\n{character_info}\n"
        if context:
            prompt += f"Additional context: {context}\n\n"
        prompt += f"Text to translate: {text}{AI_PROMPT}"

        response = self.client.completions.create(
            model="claude-2",
            prompt=prompt,
            max_tokens_to_sample=2000
        )
        return response.completion

# Example usage
if __name__ == "__main__":
    client = AnthropicClient()
    text = "Hello, world!"
    translated = client.translate(text, "Spanish")
    print(f"Original: {text}")
    print(f"Translated: {translated}")

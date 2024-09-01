from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from src.utils.config import Config
from src.translation.character_context import CharacterContextManager

import os

class AnthropicClient:
    def __init__(self, character_context):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.character_context = character_context

    def translate(self, text, target_language):
        character_info = self.character_context.generate_context_string()
        prompt = f"{HUMAN_PROMPT}Translate the following text to {target_language}. "
        prompt += f"Consider this context about the characters:\n{character_info}\n"
        prompt += f"Text to translate: {text}{AI_PROMPT}"

        response = self.client.completions.create(
            model="claude-2",
            prompt=prompt,
            max_tokens_to_sample=2000
        )
        return response.completion

# Example usage
if __name__ == "__main__":
    ccm = CharacterContextManager('characters.json')
    client = AnthropicClient(ccm)
    text = "Martina looked at Nolan, wondering if he understood the gravity of the situation."
    translated = client.translate(text, "Spanish")
    print(f"Original: {text}")
    print(f"Translated: {translated}")

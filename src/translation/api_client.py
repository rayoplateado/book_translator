from anthropic import Anthropic
from src.utils.config import Config
from src.translation.character_context import CharacterContextManager
import json
import os

class AnthropicClient:
    def __init__(self, character_context):
        self.client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        self.character_context = character_context
        self.translator_config = self.load_translator_config()

    def load_translator_config(self):
        config_path = os.path.join(os.path.dirname(__file__), 'translation_config.json')
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        with open(config_path, 'r') as f:
            return json.load(f)

    def translate(self, text, target_language, source_language="Spanish"):
        character_info = self.character_context.generate_context_string()
        config = self.translator_config

        system_prompt = f"{config['translator_role'].replace('target language', target_language)}\n\n"
        system_prompt += f"Style conventions: {config['style_conventions']}\n"
        system_prompt += f"Idiomatic expressions: {config['idiomatic_expressions']}\n"
        system_prompt += f"Formatting instructions: {config['formatting_instructions']}\n"
        system_prompt += f"File format: {config['file_format']}\n"
        system_prompt += f"File handling: {config['file_handling']}\n"
        system_prompt += f"File naming: {config['file_naming']}\n"
        system_prompt += f"Output format: {config['output_format']}\n"
        system_prompt += f"Default instructions: {config['default_instructions']}\n"
        system_prompt += f"Context: {config['context']}\n"
        system_prompt += f"Additional notes: {config['additional_notes']}\n"
        system_prompt += f"Character information:\n{character_info}\n"

        user_prompt = f"Source language: {source_language}\n"
        user_prompt += f"Target language: {target_language}\n\n"
        user_prompt += f"Text to translate:\n{text}\n"

        response = self.client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4096,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        return response.content[0].text

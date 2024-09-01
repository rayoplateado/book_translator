# src/translation/universal_translator.py

from typing import List, Dict
from src.translation.api_client import AnthropicClient
from src.translation.character_context import CharacterContextManager

class UniversalTextTranslator:
    def __init__(self, character_context: CharacterContextManager, max_chunk_size: int = 7500):
        self.client = AnthropicClient(character_context)
        self.character_context = character_context
        self.max_chunk_size = max_chunk_size
        self.translation_memory: Dict[str, str] = {}

    def translate_document(self, input_file: str, output_file: str, target_language: str):
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        translated_content = self.translate(content, target_language)

        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(translated_content)

        print(f"Translation completed. Output saved to {output_file}")

    def translate(self, text: str, target_language: str) -> str:
        chunks = self.split_into_chunks(text)
        translated_chunks = self.translate_chunks(chunks, target_language)
        return self.merge_chunks(translated_chunks)

    def split_into_chunks(self, content: str) -> List[str]:
        chunks = []
        current_chunk = ""
        for paragraph in content.split('\n\n'):
            if len(current_chunk) + len(paragraph) > self.max_chunk_size:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph
            else:
                current_chunk += "\n\n" + paragraph
        if current_chunk:
            chunks.append(current_chunk.strip())
        return chunks

    def translate_chunks(self, chunks: List[str], target_language: str) -> List[str]:
        translated_chunks = []
        context = ""
        for i, chunk in enumerate(chunks):
            character_info = self.character_context.generate_context_string()
            prompt = f"""Translate the following text to {target_language}.
            Previous context: {context[:500]}...

            Character information:
            {character_info}

            Text to translate:
            {chunk}

            Important:
            1. Maintain consistency with previous translations and character information.
            2. Preserve the original formatting, including paragraph breaks.
            3. Keep proper nouns and technical terms unchanged unless there's a well-known translation.
            4. Translate idioms and cultural references appropriately for the target language.
            """

            translated_chunk = self.client.translate(prompt, target_language)
            translated_chunks.append(translated_chunk)

            # Update context for next chunk
            context = f"{context[-1000:]} {translated_chunk[:1000]}"

            # Update translation memory
            self.update_translation_memory(chunk, translated_chunk)

            print(f"Translated chunk {i+1}/{len(chunks)}")

        return translated_chunks

    def merge_chunks(self, chunks: List[str]) -> str:
        return "\n\n".join(chunks)

    def update_translation_memory(self, source: str, translation: str):
        # Simple word-level translation memory
        source_words = source.split()
        translation_words = translation.split()
        for s, t in zip(source_words, translation_words):
            if len(s) > 3 and len(t) > 3:  # Ignore very short words
                self.translation_memory[s.lower()] = t

    def post_process(self, text: str) -> str:
        words = text.split()
        for i, word in enumerate(words):
            lower_word = word.lower()
            if lower_word in self.translation_memory:
                words[i] = self.translation_memory[lower_word]
        return ' '.join(words)

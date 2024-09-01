# src/translation/translator.py

import os
import sys
import argparse

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.translation.character_context import CharacterContextManager
from src.translation.universal_translator import UniversalTextTranslator
from src.translation.epub_handler import EPUBHandler

class BookTranslator:
    def __init__(self, characters_file):
        self.character_context = CharacterContextManager(characters_file)
        self.universal_translator = UniversalTextTranslator(self.character_context)
        self.epub_handler = EPUBHandler(self.universal_translator)

    def translate_file(self, input_file, output_file, target_language, start_chapter=None, end_chapter=None):
        # Ensure input_file is an absolute path
        input_file = os.path.abspath(input_file)
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        _, file_extension = os.path.splitext(input_file)

        if file_extension.lower() == '.epub':
            if start_chapter or end_chapter:
                total_chapters = self.epub_handler.get_chapter_count(input_file)
                print(f"Total chapters in the EPUB: {total_chapters}")

                if start_chapter and start_chapter > total_chapters:
                    raise ValueError(f"Start chapter {start_chapter} is greater than total chapters {total_chapters}")
                if end_chapter and end_chapter > total_chapters:
                    raise ValueError(f"End chapter {end_chapter} is greater than total chapters {total_chapters}")

                print(f"Translating chapters {start_chapter or 1} to {end_chapter or total_chapters}")

            self.epub_handler.process_epub(input_file, output_file, target_language, start_chapter, end_chapter)
        else:
            # Para archivos que no son EPUB, simplemente leemos y traducimos el contenido
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            translated_content = self.universal_translator.translate(content, target_language)
            print("Traducción completada:")
            print(translated_content)

def main():
    parser = argparse.ArgumentParser(description="Translate a book")
    parser.add_argument('--input', required=True, help='Input file to translate (txt or epub)')
    parser.add_argument('--output', help='Output file for translated text (not used in this version)')
    parser.add_argument('--target-language', required=True, help='Target language for translation')
    parser.add_argument('--characters-file', default='characters.json', help='JSON file with character information')
    parser.add_argument('--start-chapter', type=int, help='Starting chapter for translation (EPUB only)')
    parser.add_argument('--end-chapter', type=int, help='Ending chapter for translation (EPUB only)')

    args = parser.parse_args()

    # Handle relative paths
    input_file = os.path.join(project_root, args.input)
    characters_file = os.path.join(project_root, args.characters_file)

    if not os.path.exists(characters_file):
        print(f"Error: Characters file {characters_file} not found.")
    else:
        translator = BookTranslator(characters_file)
        translator.translate_file(input_file, args.output, args.target_language, args.start_chapter, args.end_chapter)

if __name__ == "__main__":
    main()

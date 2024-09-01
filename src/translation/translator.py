import os
import sys
import argparse

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)

from src.translation.api_client import AnthropicClient
from src.translation.character_context import CharacterContextManager

class BookTranslator:
    def __init__(self, characters_file):
        self.character_context = CharacterContextManager(characters_file)
        self.client = AnthropicClient(self.character_context)

    def translate_file(self, input_file, output_file, target_language, source_language="Spanish"):
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            content = infile.read()
            translated_content = self.client.translate(content, target_language, source_language)
            outfile.write(translated_content)
        print(f"Translation completed. Output saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Translate a book")
    parser.add_argument('--input', required=True, help='Input file to translate')
    parser.add_argument('--output', required=True, help='Output file for translated text')
    parser.add_argument('--target-language', required=True, help='Target language for translation')
    parser.add_argument('--source-language', default='Spanish', help='Source language of the text')
    parser.add_argument('--characters-file', default='characters.json', help='JSON file with character information')

    args = parser.parse_args()

    characters_file = os.path.abspath(args.characters_file)
    if not os.path.exists(characters_file):
        print(f"Error: Characters file {characters_file} not found.")
    else:
        translator = BookTranslator(characters_file)
        translator.translate_file(args.input, args.output, args.target_language, args.source_language)

if __name__ == "__main__":
    main()

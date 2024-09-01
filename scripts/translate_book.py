from src.translation.api_client import AnthropicClient
from src.translation.character_context import CharacterContextManager
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Translate a book")
    parser.add_argument('--input', required=True, help='Input file to translate')
    parser.add_argument('--output', required=True, help='Output file for translated text')
    parser.add_argument('--target-language', required=True, help='Target language for translation')
    parser.add_argument('--characters-file', default='characters.json', help='JSON file with character information')

    args = parser.parse_args()

    # Asegúrate de que la ruta al archivo de personajes sea absoluta
    characters_file = os.path.abspath(args.characters_file)

    # Verifica si el archivo existe
    if not os.path.exists(characters_file):
        print(f"Error: Characters file {characters_file} not found.")
        return

    character_context = CharacterContextManager(characters_file)
    client = AnthropicClient(character_context)

    # Aquí iría la lógica para leer el archivo de entrada, traducir por capítulos, etc.
    # Por ejemplo:
    with open(args.input, 'r') as input_file, open(args.output, 'w') as output_file:
        for line in input_file:
            translated_line = client.translate(line, args.target_language)
            output_file.write(translated_line + '\n')

    print(f"Translation completed. Output saved to {args.output}")

if __name__ == "__main__":
    main()

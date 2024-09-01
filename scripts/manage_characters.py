import argparse
import json
import os
from src.translation.character_context import CharacterContextManager

def main():
    parser = argparse.ArgumentParser(description="Manage characters for book translation")
    parser.add_argument('--file', default='characters.json', help='JSON file to store characters')
    parser.add_argument('--add', action='store_true', help='Add a new character')
    parser.add_argument('--list', action='store_true', help='List all characters')
    parser.add_argument('--name', help='Character name')
    parser.add_argument('--gender', help='Character gender')
    parser.add_argument('--description', help='Character description')
    parser.add_argument('--role', help='Character role')

    args = parser.parse_args()

    ccm = CharacterContextManager(args.file)

    if args.add:
        if not all([args.name, args.gender, args.description, args.role]):
            print("Error: All character details (name, gender, description, role) are required to add a character.")
            return
        ccm.add_character(args.name, args.gender, args.description, args.role)
        ccm.save_to_file(args.file)
        print(f"Character {args.name} added successfully.")

    if args.list:
        print(ccm.generate_context_string())

if __name__ == "__main__":
    main()

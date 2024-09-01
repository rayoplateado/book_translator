import json
import os

class CharacterContextManager:
    def __init__(self, characters_file=None):
        self.characters = {}
        if characters_file and os.path.exists(characters_file):
            self.load_from_file(characters_file)

    def load_from_file(self, filename):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Character file {filename} not found.")
        with open(filename, 'r') as f:
            self.characters = json.load(f)
        print(f"Loaded {len(self.characters)} characters from {filename}")

    def add_character(self, name, gender, description, role):
        self.characters[name] = {
            'gender': gender,
            'description': description,
            'role': role
        }

    def get_character_info(self, name):
        return self.characters.get(name, None)

    def generate_context_string(self):
        context = "Character information:\n"
        for name, info in self.characters.items():
            context += f"{name}: {info['gender']}, {info['role']}, {info['description']}\n"
        return context

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.characters, f, indent=2)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.characters = json.load(f)


# client.character_context.add_character("Martina", "Female", "18 years old, intelligent, resourceful, protagonist, trapped in a time loop", "Main character")
# client.character_context.add_character("Nolan", "Male", "Mid 20s, brilliant programmer, key to saving humanity, transported to the future", "Main character")
# client.character_context.add_character("Dot", "Male", "Appears in his 40s, dataist leader, guides Nolan, seeks to change the past", "Main character")
# client.character_context.add_character("Comma", "Female", "Appears elderly, dataist leader, seeks control, manipulates the system", "Main character")
# client.character_context.add_character("Ken", "Male", "24 years old, funny, sarcastic, dataist agent, helps Martina, impulsive", "Secondary character")
# client.character_context.add_character("Óliver", "Male", "Mid 30s, methodical, analytical, dataist agent, Martina's ally, seeks understanding", "Secondary character")
# client.character_context.add_character("Félix", "Male", "20 years old, prodigious memory, dataist retentive, becomes Comma's host", "Secondary character")
# client.character_context.add_character("África", "Female", "Early 20s, architecture student, dataist agent, helps Martina, kind", "Secondary character")
# client.character_context.add_character("Hayato", "Male", "Mid 30s, train driver, dataist agent, helps Nolan, speaks Spanish", "Secondary character")
# client.character_context.add_character("Sepa", "Male", "Appears in his 50s, dataist leader, enthusiastic, seeks solutions", "Secondary character")
# client.character_context.add_character("Valu", "Female", "Appears in her 30s, dataist leader, practical, seeks the best outcome", "Secondary character")
# client.character_context.add_character("Sam", "Male", "52 years old, dataist vigilante, experienced, impulsive, seeks control", "Secondary character")
# client.character_context.add_character("Max", "Male", "52 years old, dataist vigilante, physically imposing, aggressive, follows orders", "Secondary character")
# client.character_context.add_character("Alain", "Male", "104 years old, dataist engineer, dynamic, seeks to appear young", "Secondary character")
# client.character_context.add_character("Claudia", "Female", "90 years old, dataist engineer, brilliant, prioritizes comfort over appearance", "Secondary character")
# client.character_context.add_character("Alphonse", "Male", "11 years old, innocent, helpful, delivers a message to Martina", "Secondary character")

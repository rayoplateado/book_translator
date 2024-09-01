import json

class CharacterContextManager:
    def __init__(self):
        self.characters = {}

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
            json.dump(self.characters, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.characters = json.load(f)

# # Example usage
# if __name__ == "__main__":
#     ccm = CharacterContextManager()
#     ccm.add_character("Alice", "female", "30 years old, blonde hair", "Protagonist")
#     ccm.add_character("Bob", "male", "35 years old, Alice's older brother", "Supporting character")
#     print(ccm.generate_context_string())

from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

class Config:
    ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
    # Añade aquí otras variables de configuración según sea necesario

    @classmethod
    def get(cls, key, default=None):
        return getattr(cls, key, default)

# Uso:
# from src.utils.config import Config
# api_key = Config.get('ANTHROPIC_API_KEY')

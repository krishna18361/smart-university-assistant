import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    APP_NAME = "Smart University Assistant"
    DEBUG = os.getenv("DEBUG", "True") == "True"
    VERSION = "1.0.0"
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this-in-production")
    UPLOAD_FOLDER = "uploads"

    # PostgreSQL Configuration
    DATABASE_CONFIG = {
        "host": os.getenv("POSTGRES_HOST", "localhost"),
        "port": int(os.getenv("POSTGRES_PORT", "5432")),
        "database": os.getenv("POSTGRES_DB", "university_assistant"),
        "user": os.getenv("POSTGRES_USER", "ananthakrishna"),
        "password": os.getenv("POSTGRES_PASSWORD", "")
    }

    # MongoDB Configuration
    MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
    MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME", "smart_university_assistant")

    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

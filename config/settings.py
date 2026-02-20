# Application configuration settings

class Config:

    APP_NAME = "Smart University Assistant"

    DEBUG = True

    VERSION = "1.0.0"

    # Future database configuration (PostgreSQL)
    DATABASE_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "university_assistant",
    "user": "ananthakrishna",  # use your Mac username from whoami
    "password": ""              # leave empty for Mac default
}

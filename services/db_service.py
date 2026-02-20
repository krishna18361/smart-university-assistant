import psycopg2
from config.settings import Config


def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=Config.DATABASE_CONFIG["host"],
            port=Config.DATABASE_CONFIG["port"],
            database=Config.DATABASE_CONFIG["database"],
            user=Config.DATABASE_CONFIG["user"],
            password=Config.DATABASE_CONFIG["password"]
        )

        return connection

    except Exception as e:
        print("Database connection failed:", e)
        return None
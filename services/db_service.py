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


def save_question(question, answer):
    connection = get_db_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
        INSERT INTO questions (question, answer)
        VALUES (%s, %s);
    """

    cursor.execute(query, (question, answer))

    connection.commit()

    cursor.close()
    connection.close()

    return True
def get_all_questions():
    connection = get_db_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    query = "SELECT id, question, answer, created_at FROM questions ORDER BY created_at DESC;"

    cursor.execute(query)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    result = []

    for row in rows:
        result.append({
            "id": row[0],
            "question": row[1],
            "answer": row[2],
            "created_at": str(row[3])
        })

    return result
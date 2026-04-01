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

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO questions (question, answer)
            VALUES (%s, %s);
        """

        cursor.execute(query, (question, answer))
        connection.commit()

        return True

    except Exception as e:
        print("Error saving question:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()
def get_all_questions():
    connection = get_db_connection()

    if connection is None:
        return []

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            SELECT id, question, answer, created_at
            FROM questions
            ORDER BY created_at DESC;
        """

        cursor.execute(query)
        rows = cursor.fetchall()

        result = []

        for row in rows:
            result.append({
                "id": row[0],
                "question": row[1],
                "answer": row[2],
                "created_at": str(row[3])
            })

        return result

    except Exception as e:
        print("Error fetching questions:", e)
        return []

    finally:
        if cursor:
            cursor.close()
        connection.close()
def get_question_by_id(question_id):
    connection = get_db_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    query = """
        SELECT id, question, answer, created_at
        FROM questions
        WHERE id = %s;
    """

    cursor.execute(query, (question_id,))
    row = cursor.fetchone()

    cursor.close()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "question": row[1],
        "answer": row[2],
        "created_at": str(row[3])
    }
def update_question_by_id(question_id, new_question, new_answer):
    connection = get_db_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            UPDATE questions
            SET question = %s,
                answer = %s
            WHERE id = %s;
        """

        cursor.execute(query, (new_question, new_answer, question_id))
        connection.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print("Error updating question:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()
def delete_question_by_id(question_id):
    connection = get_db_connection()

    if connection is None:
        return False

    cursor = None

    try:
        cursor = connection.cursor()

        query = "DELETE FROM questions WHERE id = %s;"

        cursor.execute(query, (question_id,))
        connection.commit()

        return cursor.rowcount > 0

    except Exception as e:
        print("Error deleting question:", e)
        return False

    finally:
        if cursor:
            cursor.close()
        connection.close()
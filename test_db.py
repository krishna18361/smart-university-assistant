from services.db_service import get_db_connection

connection = get_db_connection()

if connection:
    print("Database connected successfully!")
    connection.close()
else:
    print("Database connection failed.")
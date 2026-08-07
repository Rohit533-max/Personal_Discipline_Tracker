import sqlite3

DATABASE_NAME = 'personal_discipline_tracker.db'

def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        priority TEXT,
        created_at DATE DEFAULT CURRENT_DATE,
        active INTEGER DEFAULT 1
        )
        """)

    connection.commit()

    connection.close()

if __name__ == "__main__":
    create_table()
    print("Database is ready")
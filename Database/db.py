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
        created_at DATE DEFAULT CURRENT_DATE)
        """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_records(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER NOT NULL,
        date DATE NOT NULL,
        completed INTEGER DEFAULT 0,
        completed_time TIME,
        FOREIGN KEY (task_id) REFERENCES tasks(id),
        UNIQUE(task_id, date)
        )
        """)
    connection.commit()

    connection.close()


if __name__ == "__main__":
    create_table()
    print("Database is ready")
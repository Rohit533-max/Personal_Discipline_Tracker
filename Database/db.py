import sqlite3

def get_connection():
    DB = "personal_discipline_tracker.db"

    connection = sqlite3.connect(DB)

    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXIST tasks(
        id INT PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
        priority TEXT NOT NULL)""")

    connection.commit()
    connection.close()

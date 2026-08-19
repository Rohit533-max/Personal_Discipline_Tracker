import sqlite3

def get_connection():
    DB = "personal_discipline_tracker.db"

    connection = sqlite3.connect(DB)

    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        priority TEXT NOT NULL,
        task_date DATE NOT NULL,
        archived INTEGER NOT NULL DEFAULT 0)""")

    connection.commit()
    connection.close()

def daily_records():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS daily_record(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER NOT NULL,
        date DATE NOT NULL,
        completed BOOLEAN NOT NULL DEFAULT 0,
        completed_at DATETIME,
        
        FOREIGN KEY (task_id) REFERENCES tasks(id),
        UNIQUE (task_id,date))""")

    #unique does don't allow same thing to be entered twice


    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
    print("Database created")
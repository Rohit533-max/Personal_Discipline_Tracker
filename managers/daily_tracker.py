from datetime import datetime
from Database.db import get_connection



def mark_completed(task_id):
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO daily_records(task_id, date, completed, completed_time) 
        VALUES (?,?,?,?)""",
        (
            task_id,
            now.date().isoformat(),
            1,
            now.time().isoformat()
        ))
    connection.commit()
    connection.close()

def mark_incomplete(task_id):
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE daily_records SET completed = ? WHERE task_id = ? AND date = ?", (0,task_id,now.date().isoformat()))

    connection.commit()
    connection.close()

def is_completed(task_id):
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT completed FROM daily_records WHERE task_id = ? AND date = ?", (task_id,now.date().isoformat()))

    result = cursor.fetchone()
    connection.close()

    if result is None:
        return False
    return result[0] ==1
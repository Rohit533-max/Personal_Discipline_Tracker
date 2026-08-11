from datetime import datetime
from Database.db import get_connection



def create_today_records():
    now = datetime.now().date().isoformat()

    connection = get_connection()
    cursor = connection.cursor()

    #get all current task
    cursor.execute("SELECT id FROM tasks")
    tasks = cursor.fetchall()

    for task in tasks:
        task_id = task[0]

        #create today record only if not exist
        cursor.execute("SELECT id FROM daily_records WHERE task_id = ? AND date = ?", (task_id,now))
        existing_record = cursor.fetchone()

        if existing_record is None:
            cursor.execute("""
            INSERT INTO daily_records
                (task_id,date,completed) VALUES (?,?,?)""",(task_id,now,0))
    connection.commit()
    connection.close()

def mark_completed(task_id):
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE daily_records SET completed= ?, completed_time = ? 
        WHERE task_id = ? AND date = ?""",
        (
            1,
            now.time().isoformat(),
            task_id,
            now.date().isoformat()
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

def get_today_records():
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM daily_records WHERE date = ?", (now.date().isoformat(),))

    records = cursor.fetchall()

    connection.close()

    return records

def get_completed_task():
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM daily_records WHERE date = ? AND completed = 1",(now.date().isoformat(),))

    result = cursor.fetchall()
    connection.close()

    return result

def get_completed_count():
    now = datetime.now()
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM daily_records WHERE date = ? AND completed = 1", (now.date().isoformat(),))

    count = cursor.fetchone()[0]

    connection.close()
    return count

def get_total_task():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")

    count = cursor.fetchone()[0]
    connection.close()
    return count

def get_completion_percentage():
    total = get_total_task()
    completed = get_completed_count()

    if total == 0:
        return 0
    return (completed / total) *100

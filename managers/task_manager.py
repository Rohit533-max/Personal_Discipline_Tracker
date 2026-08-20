from Database.db import get_connection
from Database.models import Task
from datetime import date

now = date.today()

def add_task(task):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO tasks('name','priority','task_date') VALUES(?,?,?)""",(
        task.name,
        task.priority,
        now
    ))
    connection.commit()
    connection.close()

def get_task():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    connection.close()
    return result

def update_task(task_id,name,priority):
    connection = get_connection()
    try:
        cursor =  connection.cursor()

        cursor.execute("UPDATE tasks SET name = ?, priority = ? WHERE id = ?",(name,priority,task_id))
        if cursor.rowcount ==0:
            return "Task not found"
        connection.commit()
        return "Task updated successfully"
    finally:
        connection.close()

def del_task(task_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
        if cursor.rowcount ==0:
            return "Invalid Task ID"
        
        connection.commit()
        return "Task deleted successfully"
    finally:
        connection.close()
        
def add_record(task):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO daily_record (task_id,date) VALUES (?,?)",(task['id'],now))

    connection.commit()
    connection.close()

def get_daily_records():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM daily_record WHERE date = ?",(now,))
    daily_records = cursor.fetchall()

    connection.close()
    return daily_records

def mark_completed(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE daily_record SET completed = 1, completed_at = CURRENT_TIMESTAMP WHERE task_id = ? AND date = ?",(task_id,now))

    connection.commit()
    connection.close()

def mark_incompleted(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE daily_record SET completed = 0 WHERE task_id = ? AND date = ?",(task_id,now))

    connection.commit()
    connection.close()

def is_completed_today(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT completed from daily_record WHERE task_id = ? AND date = ?",(task_id,now))

    result = cursor.fetchone()

    connection.close()
    return result if not None and result[0] == 1 else "No Task Found"



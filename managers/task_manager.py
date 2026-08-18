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
        

from Database.db import get_connection
from Database.models import Task



def add_task(task):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO tasks('name','priority') VALUES(?,?)""",(
        task.name,
        task.priority
    ))
    connection.commit()
    connection.close()

def get_task():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    result = cursor.fetchall()
    connection.close()

    for r in result:
        print(r)

def update_task(task_id,name,priority):
    connection = get_connection()
    cursor =  connection.cursor()

    cursor.execute("UPDATE tasks SET name = ?, priority = ? WHERE id = ?",(name,priority,task_id))

    connection.commit()
    connection.close()

def del_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?",(task_id,))
    connection.commit()
    connection.close()

from Database.db import get_connection

def add_task(task):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO Tasks (name,description,priority) VALUES(?,?,?)
    """,
    (
        task.name,
        task.description,
        task.priority
    ))

    connection.commit()
    connection.close()

def get_tasks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Tasks WHERE active = 1")
    task = cursor.fetchall()

    return task

    
        

def del_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        return "404 Not Found"

    return "Task Deleted Successfully"

    connection.commit()
    connection.close()

def update_task(task_id, new_name = None, new_description = None, new_priority = None):
    connection = get_connection()
    cursor = connection.cursor()

    updates = []  #contain pieces of SQL
    values = []

    if new_name is not None:
        updates.append("name = ?") 
        values.append(new_name)

    if new_description is not None:
        updates.append("description = ?")
        values.append(new_description)

    if new_priority is not None:
        updates.append("priority = ?")
        values.append(new_priority)

    if not updates:
        connection.close() 

    set_clause = ", ".join(updates)

    query =  f"UPDATE Tasks SET {set_clause} WHERE id =  ?"
    values.append(task_id)
    cursor.execute(query, values)


    connection.commit()
    connection.close()


def archive_task(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE Tasks SET active = ? WHERE id = ?", (0,task_id))

    connection.commit()
    connection.close()
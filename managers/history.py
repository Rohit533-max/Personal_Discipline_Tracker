from Database.db import get_connection

def get_records_by_date(date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT daily_records.task_id,
            tasks.name,
            daily_records.completed,
            daily_records.completed_time
        FROM daily_records
        JOIN tasks
        ON daily_records.task_id = tasks.id
        WHERE daily_records.date = ?""",(date,))

    records = cursor.fetchall()

    connection.close()
    return records

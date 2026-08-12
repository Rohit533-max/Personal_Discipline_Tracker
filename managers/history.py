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

def get_history_dates():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT DISTINCT date
    FROM daily_records
    ORDER BY date DESC""")

    dates = cursor.fetchall()

    connection.close()

    return dates

def get_day_progress(date):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM daily_records WHERE date = ?",(date,))
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM daily_records WHERE date = ? AND completed = 1", (date,))
    completed = cursor.fetchone()[0]

    connection.close()

    if total == 0:
        percentage = 0
    else:
        percentage = (completed / total) * 100

    return completed, total, percentage


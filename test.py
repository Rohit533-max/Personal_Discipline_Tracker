from managers.daily_tracker import mark_completed
from managers.task_manager import get_tasks

tasks = get_tasks()
for t in tasks:
    print(t)
mark_completed(1)
print("Task marked completed")
from Database.models import Task
from managers.task_manager import get_tasks, update_task, add_task,del_task

# task = Task("Cricket", "Morning", "Medium")
# add_task(task)




tasks = get_tasks()
for t in tasks:
    print(t)

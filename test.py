from Database.db import get_connection
from managers.task_manager import add_task, get_task, del_task,update_task
from Database.models import Task

task = Task("Python","High")
# add_task(task)

update_task(4,"Book reading","High")


if __name__ == "__main__":
    get_task()
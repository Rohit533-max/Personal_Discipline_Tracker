import customtkinter as ctk
from managers.task_manager import add_task as save_task, get_tasks
from Database.models import Task
class Taskpage(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        self.pack(fill = "both", expand = True)

        title = ctk.CTkLabel(self,text="Task Manager", font=("Arial",25))

        title.pack(pady = 20)

        self.name_entry = ctk.CTkEntry(
            self,
            placeholder_text= "Task name"
        )

        self.name_entry.pack(padx = 20, pady = 0)

        self.description = ctk.CTkEntry(
            self,
            placeholder_text= "Description"
        )
        self.description.pack(padx = 20, pady = 10)

        self.priority = ctk.CTkEntry(
            self,
            placeholder_text= "Priority"
        )
        self.priority.pack(padx = 20, pady = 10)

        self.add_button = ctk.CTkButton(
            self,
            text= "Add Task",
            command = self.add_task
        )
        self.add_button.pack(
            padx = 20,
            pady = 20
        )
        self.load_task_frame = ctk.CTkFrame(
            self,
            fg_color= "Transparent"
        )
        self.load_task_frame.pack(
            fill = "both",
            expand = "True",
            padx = 20,
            pady = 20
        )
        self.load_task()
        
    def add_task(self):
        name = self.name_entry.get()
        description = self.description.get()
        priority = self.priority.get()

        task = Task(name,description,priority)
        save_task(task)

    def load_task(self):
        tasks = get_tasks()
        print(tasks)



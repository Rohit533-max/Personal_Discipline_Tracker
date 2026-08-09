import customtkinter as ctk
from managers.task_manager import add_task as save_task, get_tasks,del_task
from Database.models import Task
from managers.daily_tracker import mark_completed, mark_incomplete
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
        self.task_list_frame = ctk.CTkFrame(
            self,
            fg_color= "White"
        )
        self.task_list_frame.pack(
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
        #remove old task frames
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        #get current tasks from database
        tasks = get_tasks()
#create a frame for each task
        for task in tasks:
            task_frame = ctk.CTkFrame(
                self.task_list_frame
            )

            task_frame.pack(
                fill = "x",
                padx = 10,
                pady = 5
            )
            #checkbox
            checkbox = ctk.CTkCheckBox(
                task_frame,
                text = task[1]
            )
            checkbox.pack(anchor = "w", padx =10, pady = 5)
#Put the task name and other values inside the frame..
            name_label = ctk.CTkLabel(
                task_frame,
                text=task[1],
                font=("Arial",16,"bold")
            )
            name_label.pack(anchor = "w", padx = 10, pady=5)

            description_label = ctk.CTkLabel(task_frame,text=task[2])
            description_label.pack(anchor = "w", padx=10)

            priority_label = ctk.CTkLabel(task_frame,text=f"Priority:{task[3]}")
            priority_label.pack(anchor = "w", padx = 10, pady = 5)


            delete_button = ctk.CTkButton(
                task_frame,
                text="Delete",
                command = lambda:self.handle_delete(task[0])
            )
            delete_button.pack(padx = 10, pady = 5)
# after deleting a task we want ui to refresh
    def handle_delete(self,task_id):
        del_task(task_id)
        self.load_task()

    def toggle_task(self,task_id,checkbox):
        if checkbox.get():
            mark_completed(task_id)
        else:
            mark_incomplete(task_id)
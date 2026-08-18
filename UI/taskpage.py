import customtkinter
from Database.models import Task
from managers.task_manager import add_task as save_task, del_task, get_task

class ask_task(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        label = customtkinter.CTkLabel(self,text="Welcome to Taskpage", font=("Arial",26))
        label.pack()

        self.task_name = customtkinter.CTkEntry(self,placeholder_text='Task')
        self.task_name.pack(padx = 10, pady = 20)

        self.task_priority = customtkinter.CTkComboBox(self,values = ['Low','Mid','High'])
        self.task_priority.pack(padx = 10, pady = 20)

        self.add_button = customtkinter.CTkButton(self,text = "Add Task", command= self.add_task)
        self.add_button.pack(padx = 15)

        self.task_container = customtkinter.CTkScrollableFrame(self)
        self.task_container.pack(fill= 'both', expand = True, padx = 15, pady = 10)

        self.display()

    def display(self):
        tasks = get_task()
        for task in tasks:
            id = task[0]
            name = task[1]
            priority = task[2]

            task_frame = customtkinter.CTkFrame(self.task_container)
            task_frame.pack(fill = 'x', padx =10, pady = 5)

            task_label = customtkinter.CTkLabel(
                task_frame,
                text=f"{name} | Priority: {priority}"
            )
            task_label.pack(side = 'left')

            delete_button = customtkinter.CTkButton(
                task_frame,
                text= "Delete",
                command=lambda task_id = id: self.delete(task_id)
            )
            delete_button.pack(side = 'right')


    def delete(self,task_id):
        del_task(task_id)

    def add_task(self):
        name = self.task_name.get()
        priority = self.task_priority.get()

        task = Task(name,priority)
        save_task(task)

    
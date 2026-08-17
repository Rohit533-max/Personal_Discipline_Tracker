import customtkinter

class ask_task(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Taskpage")
        self.geometry("600x600")

        label = customtkinter.CTkLabel(self,text="Welcome to Taskpage", font=("Arial",26))
        label.pack()

        task_name = customtkinter.CTkEntry(self,placeholder_text='Task')
        task_name.pack(padx = 10, pady = 20)

        task_priority = customtkinter.CTkComboBox(self,values = ['Low','Mid','High'])
        task_priority.pack(padx = 10, pady = 20)
       
        add_button = customtkinter.CTkButton(self,text = "Add Task")
        add_button.pack(padx = 15)

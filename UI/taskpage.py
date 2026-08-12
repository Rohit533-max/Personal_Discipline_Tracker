import customtkinter as ctk
from managers.task_manager import add_task as save_task, get_tasks,del_task
from Database.models import Task
from managers.daily_tracker import mark_completed, mark_incomplete,get_total_task,get_completed_count,get_completion_percentage, create_today_records,is_completed
from managers.streak import get_longest_streak, get_current_streak

class Taskpage(ctk.CTkFrame):

    def __init__(self,parent):
        super().__init__(parent)

        self.pack(fill = "both", expand = True)

        title = ctk.CTkLabel(self,text="Task Manager", font=("Arial",25))

        title.pack(pady = 20)
#Progress lable
        self.progress_label = ctk.CTkLabel(
            self,
            text="Today's Progress"
        )
        self.progress_label.pack(pady = 10)

        self.progress_value_label = ctk.CTkLabel(
            self,
            text= "0 / 0 (0%)"
        )
        self.progress_value_label.pack(pady = 5)

    #Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            self
        )
        self.progress_bar.pack(padx = 30, pady = 10, fill = "x")



        self.name_entry = ctk.CTkEntry(
            self,
            placeholder_text= "Task name")

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
        self.current_streak_label = ctk.CTkLabel(
            self,
            text="Current Streak: 0"
        )
        self.current_streak_label.pack(
            pady = 10
        )

        self.longetst_streak_label = ctk.CTkLabel(
            self,
            text= "Longest Streak: 0"
        )
        self.longetst_streak_label.pack(pady = 10)
        create_today_records()
        self.load_task()
        self.update_progress()
        self.update_streak_display()
    def add_task(self):
        name = self.name_entry.get()
        description = self.description.get()
        priority = self.priority.get()

        task = Task(name,description,priority)
        save_task(task)

        create_today_records()
        self.load_task()
        self.update_progress()

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
            checkbox.configure(command = lambda task_id = task[0], cb = checkbox: self.toggle_task(task_id,cb))
            if is_completed(task[0]):
                checkbox.select()
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

        # self.current_streak_label = ctk.CTkLabel(
        #     self,
        #     text="Current Streak: 0"
        # )
        # self.current_streak_label.pack(
        #     pady = 10
        # )

        # self.longetst_streak_label = ctk.CTkLabel(
        #     self,
        #     text= "Longest Streak: 0"
        # )
        # self.longetst_streak_label.pack(pady = 10)
    def update_streak_display(self):

        current = get_current_streak()
        longest = get_longest_streak()

        self.current_streak_label.configure(
            text = f"🔥 Current Streak: {current} days"
        )
        self.longetst_streak_label.configure(
            text = f"🏆 Longest Streak: {longest} days"
        )

    def update_progress(self):
        total = get_total_task()
        completed = get_completed_count()
        percentage = get_completion_percentage()

        self.progress_value_label.configure(
            text = f"{completed} / {total} ({percentage: .0f}%)"
        )
        self.progress_bar.set(
            percentage/100
        )

# after deleting a task we want ui to refresh
    def handle_delete(self,task_id):
        del_task(task_id)
        create_today_records()
        self.load_task()
        self.update_progress()
        self.update_streak_display()


    def toggle_task(self,task_id,checkbox):
        if checkbox.get():
            mark_completed(task_id)
        else:
            mark_incomplete(task_id)

        self.update_progress()
        self.update_streak_display()
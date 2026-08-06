import customtkinter as ctk

from UI.taskpage import Taskpage

app = ctk.CTk()

app.title("Personal Discipline Tracker")
app.geometry("600x500")
app.configure(fg_color = "#1D1717")

task_page = Taskpage(app)

app.mainloop()
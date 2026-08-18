from UI.taskpage import ask_task
import customtkinter


app = customtkinter.CTk()
app.geometry("600x400")

task_page = ask_task(app)
task_page.pack(fill = "both", expand = True)
app.mainloop()
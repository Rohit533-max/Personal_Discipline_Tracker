import customtkinter as ctk

from UI.taskpage import Taskpage

app = ctk.CTk()

app.title("Personal Discipline Tracker")
app.geometry("600x500")
app.configure(fg_color = "#1D1717")

task_page = Taskpage(app)

app.mainloop()
from Database.db import create_table

def main():
    create_table()
    print("Database is ready")

if __name__ == "__main__":
    main()


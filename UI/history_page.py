import customtkinter as ctk
from managers.history import get_history_dates

class HistoryPage(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(parent)

        title = ctk.CTkLabel(
            self,
            text="History",
            font=("Arial",24)
        )
        title.pack(pady=20)

        dates = get_history_dates()
        for date in dates:

            button = ctk.CTkButton(
                self,
                text= date[0],
                command=lambda d=date[0]: self.show_date(d)
            )
            button.pack(pady = 5)

    def show_date(self,date):
        records = get_history_dates()

        for record in records:
            print(record)

            
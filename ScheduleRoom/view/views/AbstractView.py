import tkinter as tk
from tkcalendar import Calendar, DateEntry

class AbstractView:

    FONTE_PADRAO = ("Arial", "10")

    def __init__(self, root):
        self.root = root

       # self.root.title = "Booking Room - UniFecaf"
        self.root.maxsize(1920, 1080)
        self.root.geometry("1050x720")
        self.root.configure(background="#0B5394") 

        self.main_container = tk.Frame(self.root, background="#0B5394")
        self.main_container.pack()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

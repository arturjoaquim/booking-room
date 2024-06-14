from tkinter import ttk


class AbstractView:

    def __init__(self, root):
        self.root = root

        self.root.title = "Booking Room - UniFecaf"
        self.root.maxsize(1000, 400)
        self.root.configure(background="#0B5394") 

        self.main_container = ttk.Frame(root, padding=10)

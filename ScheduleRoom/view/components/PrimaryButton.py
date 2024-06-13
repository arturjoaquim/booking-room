from tkinter import Frame, Button


class PrimaryButton:

    def __init__(self, text: str, command, parent: Frame):
        self.button = Button(parent, background="#29a649", foreground="white")
        self.button["text"] = text
        self.button["font"] = ("Calibri", "8")
        self.button["width"] = 12
        self.button["command"] = command
        self.button.pack()

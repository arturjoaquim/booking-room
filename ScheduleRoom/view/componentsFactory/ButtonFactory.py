from tkinter import Button, Widget

class ButtonFactory:
    
    @staticmethod
    def createPrimaryButton(text: str, command, parent: Widget):
       # ttk.Style().configure("TButton", padding=6, relief="flat",
        #    background="#29a649", foreground="white)
        primaryButton = Button(parent, bg="#29a649", fg="white")
        primaryButton["text"] = text
        primaryButton["font"] = ("Calibri", "8")
        primaryButton["width"] = 12
        primaryButton["command"] = command
       # primaryButton.pack(pady=10, padx=5)

        return primaryButton

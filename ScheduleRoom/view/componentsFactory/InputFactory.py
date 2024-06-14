from tkinter import Entry, Widget
from scheduleroom.view.views.AbstractView import AbstractView


class InputFactory:

    @staticmethod
    def createInputText(parent: Widget):
        inputText = Entry(parent)
        inputText["width"] = 30
        inputText["font"] = AbstractView.FONTE_PADRAO
       # inputText.pack(pady=5, padx=5)

        return inputText
    
    @staticmethod
    def createInputSecret(parent: Widget):
        inputSecret = Entry(parent)
        inputSecret["width"] = 30
        inputSecret["font"] = AbstractView.FONTE_PADRAO
        inputSecret["show"] = "*"
       # inputSecret.pack(pady=5, padx=5)

        return inputSecret
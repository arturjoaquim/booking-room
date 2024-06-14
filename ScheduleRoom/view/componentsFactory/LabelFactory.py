from tkinter import Label, Widget
from scheduleroom.view.views.AbstractView import AbstractView

class LabelFactory:

    @staticmethod
    def createNormalLabel(parent: Widget, text: str):
        normalLabel = Label(parent, text=text, background="#0B5394", foreground="white", font=AbstractView.FONTE_PADRAO)
        return normalLabel

    @staticmethod
    def createSmallLabel():
        pass
    
    @staticmethod
    def createBigLabel():
        pass

    @staticmethod
    def createBoldLabel():
        pass
from tkinter.ttk import Widget, Notebook
from scheduleroom.view.views.ScheduleView import ScheduleView

class NavbarFactory:

    def createNavbarDefaultUser(parent: Widget):
        navbar = Notebook()
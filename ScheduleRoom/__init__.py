from scheduleroom.model.DAOs.BookingDAO import BookingDAO
from scheduleroom.model.ConnectionFactory import ConnectionFactory  
from scheduleroom.view.views.LoginView import LoginView
from tkinter import *
print("Oi")

root = Tk()
LoginView(root)
root.mainloop()
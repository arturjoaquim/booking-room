import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from scheduleroom.view.views.AbstractView import AbstractView
from scheduleroom.view.componentsFactory.ButtonFactory import ButtonFactory
from scheduleroom.view.componentsFactory.InputFactory import InputFactory
from scheduleroom.view.componentsFactory.LabelFactory import LabelFactory

class ScheduleView(AbstractView):
    def __init__(self, master):
        super.__init__(master)

     #   self.primeiroContainer = Frame(master, background="#0B5394")
      #  self.primeiroContainer.pack(side=LEFT, anchor=NW)

       # self.segundoContainer = Frame(master, background="#0B5394")
        #self.segundoContainer.pack(side=RIGHT,anchor=NE)
        self.navbar = ttk.Notebook(self.main_container)
        self.navbar.add()

        self.BtCalendario = ButtonFactory.createPrimaryButton("Data", self.calendario, self.main_container)
        self.BtCalendario.pack()
    
        self.caixa_data = InputFactory.createInputText(self.main_container)
        self.caixa_data.pack()

        self.periodo_label = LabelFactory.createNormalLabel(self.main_container, "Labs:")
        self.periodo_label.pack()

        self.lab_listbox = Listbox(self.main_container, height=4)
        self.lab_listbox.insert(tk.END, "LabI")
        self.lab_listbox.insert(tk.END, "LabII")
        self.lab_listbox.insert(tk.END, "LabIII")
        self.lab_listbox.insert(tk.END, "LabIV")
        self.lab_listbox.pack()

        self.select = Button(self.main_container, text="Selecionar", command=self.get_selection, background="#29a649", foreground="white")
        self.select.pack(side=tk.BOTTOM, pady=10)

        self.manha= Button(self.main_container,text="Manhã", background="#29a649", foreground="white")
        self.manha.pack(side=tk.LEFT)
        self.noite= Button(self.main_container,text="Noite", background="#29a649", foreground="white")
        self.noite.pack(side=tk.RIGHT)

    def calendario(self):
        self.calendario1 = Calendar(self.main_container,fg="blue", bg="gray", locale="pt_br")
        self.calendario1.pack()

        self.calldata = Button(self.main_container,text="Inserir Data", command=self.print_data, background="#29a649", foreground="white")
        self.calldata.pack()

    def print_data(self):
       dataIni = self.calendario1.get_date()
       self.calendario1.destroy()
       self.caixa_data.delete(0, END)
       self.caixa_data.insert(END, dataIni)
       self.calldata.destroy()
        
    def get_selection(self):
        selected_period = self.lab_listbox.get(self.lab_listbox.curselection()[0])


if (__name__ == "__main__"):

    cadastro = Tk()
    cadastro.configure(background="#0B5394")
    cadastro.geometry("500x300")
    ScheduleView(cadastro)  
    cadastro.mainloop()
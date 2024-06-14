from tkinter import *
from tkcalendar import Calendar, DateEntry

class ScheduleView:
    def __init__(self, master):
        self.primeiroContainer = Frame(master, background="#0B5394")
        self.primeiroContainer.pack(side=LEFT, anchor=NW)

        self.segundoContainer = Frame(master, background="#0B5394")
        self.segundoContainer.pack(side=RIGHT,anchor=NE)


        self.BtCalendario = Button(self.primeiroContainer,text="Data", command=self.calendario, background="#29a649", foreground="white")
        self.BtCalendario.pack()
    
        self.caixa_data = Entry(self.primeiroContainer)
        self.caixa_data.pack()

        self.periodo_label = Label(self.segundoContainer, text="Labs:", background="#29a649", foreground="white")
        self.periodo_label.pack()

        self.lab_listbox = Listbox(self.segundoContainer, height=4)
        self.lab_listbox.insert(END, "LabI")
        self.lab_listbox.insert(END, "LabII")
        self.lab_listbox.insert(END, "LabIII")
        self.lab_listbox.insert(END, "LabIV")
        self.lab_listbox.pack()

        self.select = Button(self.segundoContainer, text="Selecionar", command=self.get_selection, background="#29a649", foreground="white")
        self.select.pack(side=BOTTOM, pady=10)

        self.manha= Button(self.segundoContainer,text="Manhã", background="#29a649", foreground="white")
        self.manha.pack(side=LEFT)
        self.noite= Button(self.segundoContainer,text="Noite", background="#29a649", foreground="white")
        self.noite.pack(side=RIGHT)

    def calendario(self):
        self.calendario1 = Calendar(self.primeiroContainer,fg="blue", bg="gray", locale="pt_br")
        self.calendario1.pack()

        self.calldata = Button(self.primeiroContainer,text="Inserir Data", command=self.print_data, background="#29a649", foreground="white")
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
  #  cadastro.configure(background="#0B5394")
    cadastro.geometry("500x300")
    ScheduleView(cadastro)  
    cadastro.mainloop()
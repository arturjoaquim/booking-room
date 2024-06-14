import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from scheduleroom.view.views.AbstractView import AbstractView
from scheduleroom.view.componentsFactory.ButtonFactory import ButtonFactory
from scheduleroom.view.componentsFactory.InputFactory import InputFactory
from scheduleroom.view.componentsFactory.LabelFactory import LabelFactory
from scheduleroom.model.ConnectionFactory import ConnectionFactory
from scheduleroom.model.DAOs.RoomDAO import RoomDAO

class ScheduleView(AbstractView):
    
    def __init__(self, root):

        super().__init__(root)
        self.root = root
        self.root.title("Booking Room - Reserva de Sala")
        self.main_container.pack(expand=True)
        self.formGrid = tk.Frame(self.main_container)
        self.formGrid.pack(expand=True, ipadx=5, ipady=5)

        self.BtCalendario = ButtonFactory.createPrimaryButton("Data", self.calendario, self.formGrid)
        self.BtCalendario.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    
        self.caixa_data = InputFactory.createInputText(self.formGrid)
        self.caixa_data.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        self.periodSelected = tk.StringVar()
        self.manha = ttk.Radiobutton(self.formGrid, text="Manha", value="Manha", variable=self.periodSelected)
        self.manha.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.noite = ttk.Radiobutton(self.formGrid, text="Noite", value="Noite", variable=self.periodSelected)
        self.noite.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.labs_label = LabelFactory.createNormalLabel(self.formGrid, "Labs:")
        self.labs_label.grid(row=2, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        self.lab_listbox = tk.Listbox(self.formGrid, height=4)

        # CUIDADO MÁ PRÁTICA ABAIXO:
        self.getAllRooms()
        if self.rooms:
            for row in self.rooms:
                self.lab_listbox.insert(tk.END, row[1])

            self.lab_listbox.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)
        else:
            self.response_rooms = LabelFactory.createNormalLabel(self.formGrid, "Sem salas cadastradas")
            self.response_rooms.grid(row=3, column=0, columnspan=2, sticky="ew", padx=5, pady=5)

        

        self.submit = ButtonFactory.createPrimaryButton("Reservar Sala", self.get_selection, self.formGrid)
        self.submit.grid(row=4,column=0, sticky="ew", columnspan=2, padx=5, pady=5)

        self.next_page = ButtonFactory.createPrimaryButton("Ver Agenda", self.nav_to_booking_view, self.formGrid)
        self.next_page.grid(row=5, column=0, sticky="ew", columnspan=2, padx=5, pady=5)
        

    def calendario(self):
        self.calendario1 = Calendar(self.main_container,fg="blue", bg="gray", locale="pt_br")
        self.calendario1.pack(padx=5, pady=5)

        self.calldata = ButtonFactory.createPrimaryButton("Inserir Data", self.print_data, self.main_container) 
        self.calldata.pack(padx=5, pady=5)

    def print_data(self):
       dataIni = self.calendario1.get_date()
       self.calendario1.destroy()
       self.caixa_data.delete(0, tk.END)
       self.caixa_data.insert(tk.END, dataIni)
       self.calldata.destroy()
        
    def get_selection(self):
        selected_period = self.lab_listbox.get(self.lab_listbox.curselection()[0])

    def nav_to_booking_view(self):
        pass

    def getAllRooms(self):
        conexao_db = ConnectionFactory.create_connection()
        room_dao = RoomDAO(conexao_db)
        result = room_dao.findAllRooms()

        if result:
            self.rooms = result
        else:
            self.rooms = None

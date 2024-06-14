import tkinter as tk
from scheduleroom.view.views.AbstractView import AbstractView
from scheduleroom.model.ConnectionFactory import ConnectionFactory
from scheduleroom.view.componentsFactory.LabelFactory import LabelFactory
from scheduleroom.view.componentsFactory.ButtonFactory import ButtonFactory
from scheduleroom.model.DAOs.BookingDAO import BookingDAO

class QueryBookingView(AbstractView):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Confirmação de Dados")
        self.main_container.pack(expand=True)

        self.bookings_label = LabelFactory.createNormalLabel(self.main_container, "Reservas realizadas:")
        self.bookings_label.pack()
        self.booking_listbox = tk.Listbox(self.main_container, height=30, width=400)
        self.findAllBookings()

        for booking in self.all_bookings:
            result_booking_string = map(lambda item_booking: str(item_booking), booking)
            list_booking_string = list(result_booking_string)
            print()
            self.booking_listbox.insert(tk.END, "   ".join(list_booking_string))

        self.booking_listbox.pack(padx=5, pady=5, ipadx=5, ipady=5)

        self.back_schedule_button = ButtonFactory.createPrimaryButton("Reservar Salas", self.back_schedule, self.main_container)
        self.back_schedule_button.pack()

    def findAllBookings(self):
        connection_db = ConnectionFactory.create_connection()
        booking_dao = BookingDAO(connection_db)

        self.all_bookings = booking_dao.findAllBookings()

    def back_schedule(self):
        #self.main_container.destroy()
        pass

        
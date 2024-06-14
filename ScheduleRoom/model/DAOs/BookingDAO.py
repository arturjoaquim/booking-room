from scheduleroom.model.GenericDAO import GenericDAO
from scheduleroom.model.DTOs.BookingDTO import BookingDTO

class BookingDAO(GenericDAO):

    def __init__(self, connection):
        super().__init__(connection)
    
    def findBookingsByDate(self, date):
        result = self.query_all(
            """SELECT * FROM RQST_BKNG BKNG WHERE BKNG.DT_BKNG = ?""", 
            date
        )

        return result # Utilizar um cara para converter as datas

    def findAllBookings(self):
        result = self.query_all("""SELECT * FROM RQST_BKNG BKNG""")

        return result # Utilizar um cara para converter as datas

    def insertNewBooking(self, booking_DTO: BookingDTO):

        self.execute("""INSERT INTO rqst_bkng 
                     VALUES ((SELECT MAX(id_bkng) + 1 FROM rqst_bkng), 
                     "Reserva-Test", ?, 1, "Reserva teste criada em tela.", ?, ?, ?)""", 
                     booking_DTO.room_id, booking_DTO.booking_date, booking_DTO.booking_turn, booking_DTO.record_date # Preciso de um cara para converter as datas
                    )

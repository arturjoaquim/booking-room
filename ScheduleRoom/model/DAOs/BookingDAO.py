from scheduleroom.model.GenericDAO import GenericDAO

class BookingDAO(GenericDAO):

    def __init__(self, connection):
        super().__init__(connection)
    
    def findBookingsByDate(self, date):
        result = self.query_all(
            """SELECT * FROM RQST_BKNG BKNG WHERE BKNG.DT_BKNG = ?""", 
            date
        )

        return result


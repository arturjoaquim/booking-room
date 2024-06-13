class BookingDTO:

    def __init__(self, booking_id, room_id, booking_user_id, description,
                 booking_date, record_date):
        self.booking_id = booking_id
        self.room_id = room_id
        self.booking_user_id = booking_user_id
        self.description = description
        self.booking_date = booking_date
        self.record_date = record_date

class BookingDTO:

    def __init__(self, room_id, record_date, booking_date, booking_turn, booking_id=-1,
                 booking_user_id=1, description="", booking_name="",
                 ):
        self.booking_date = booking_date
        self.record_date = record_date
        self.booking_turn = booking_turn
        self.room_id = room_id
        self.booking_id = booking_id
        self.booking_name = booking_name
        self.booking_user_id = booking_user_id
        self.description = description

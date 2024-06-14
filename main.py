from scheduleroom import LoginView
from scheduleroom.model.DTOs.BookingDTO import BookingDTO
from scheduleroom.model.DAOs.BookingDAO import BookingDAO
from scheduleroom.model.ConnectionFactory import ConnectionFactory

print("teste")

booking = BookingDAO(ConnectionFactory.create_connection())

bookingList = []

for row in booking.findBookingsByDate("2024-06-25"):
    print(row)
    id_booking, nm_booking, id_room, id_usr_booking, nm_desc, dt_booking, booking_turn, dt_cad = row
    bookingList.append(BookingDTO(
        
        booking_date=dt_booking,
        record_date=dt_cad,
        booking_turn=booking_turn,
        room_id=id_room,
        booking_id=id_booking,
        booking_name=nm_booking,
        booking_user_id=id_usr_booking,
        description=nm_desc
    ))


for bookingItem in bookingList:
    print(bookingItem.booking_name)
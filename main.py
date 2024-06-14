from scheduleroom import BookingDAO, ConnectionFactory, LoginView

print("teste")

booking = BookingDAO(ConnectionFactory.create_connection())

for row in booking.findBookingsByDate("2024-06-25"):
    print(row)
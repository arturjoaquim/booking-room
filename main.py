from scheduleroom import BookingDAO;
from scheduleroom import ConnectionFactory

from scheduleroom.view.components.PrimaryButton import PrimaryButton

print("teste")

booking = BookingDAO(ConnectionFactory.create_connection())

for row in booking.findBookingsByDate("2024-06-25"):
    print(row)
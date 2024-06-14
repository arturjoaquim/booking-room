from scheduleroom.model.GenericDAO import GenericDAO

class RoomDAO(GenericDAO):

    def __init__(self, connection):
        super().__init__(connection)

    def findAllRooms(self):
        result = self.query_all("""SELECT * FROM cadroom""")

        return result

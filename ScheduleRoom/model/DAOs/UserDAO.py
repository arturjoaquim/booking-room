from scheduleroom.model.GenericDAO import GenericDAO

class UserDAO(GenericDAO):

    def __init__(self, connection):
        super().__init__(connection)

    def findUserLogin(self, username: str, password: str):
        result = self.query_first("""SELECT 1 FROM cadusr USR WHERE USR.NM_USR = ? AND USR.KEY_USR = ?""", username, password)

        if not result:
            return False

        return True
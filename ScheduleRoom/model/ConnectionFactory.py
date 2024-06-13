import sqlite3

class ConnectionFactory:

    DATABASE_FILE = "ScheduleRoomDatabase"

    def createConnection():
        return sqlite3.connect(ConnectionFactory.DATABASE_FILE)

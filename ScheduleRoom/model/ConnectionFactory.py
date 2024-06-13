import sqlite3

class ConnectionFactory:

    DATABASE_FILE = "ScheduleRoomDatabase.db"

    @staticmethod
    def create_connection():
        return sqlite3.connect(ConnectionFactory.DATABASE_FILE)

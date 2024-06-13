class GenericDAO:

    def __init__(self, connection):
        self.connection = connection

    def execute(self, sql_statement: str, *parameters):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(sql_statement, parameters)
        
    def execute_many(self, sql_statement: str, parameters: list):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.executemany(sql_statement, parameters)
        
    def query_first(self, sql_statement: str, *parameters):
        with self.connection:
            cursor = self.connection.cursor()
            result = cursor.execute(sql_statement, parameters)
            return result.fetchone()
        
    def query_all(self, sql_statement: str, *parameters):
        with self.connection:
            cursor = self.connection.cursor()
            result = cursor.execute(sql_statement, parameters)
            return result.fetchall()
        
    def setConnection(self, new_connection):
        self.connection = new_connection

    def getConnection(self):
        return self.connection
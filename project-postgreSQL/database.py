from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1 ,5, 
                                            user='postgres', 
                                            password='1234', 
                                            database='learning',
                                            host='localhost')

class CursorFromConnectionFromPool: 
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_val, exception_tb):
        if exception_val is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)


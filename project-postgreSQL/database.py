from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1 ,5, 
                                            user='postgres', 
                                            password='1234', 
                                            database='learning',
                                            host='localhost')

class ConnectionFromPool: 
    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = connection_pool.getconn()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection_pool.putconn()



# just an example, this is how we could access this connection from here
cp = ConnectionPool()
cp.connection_pool


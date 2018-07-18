from psycopg2 import pool

connection_pool = pool.SimpleConnectionPool(1 ,5, 
                                            user='postgres', 
                                            password='1234', 
                                            database='learning',
                                            host='localhost')

def connect(): 
    return psycopg2.connect()
import mysql.connector
from mysql.connector import errorcode


class MySQLConnector:

    def __init__(self):
        self.config = {
            'user': 'root',
            'host': '127.0.0.1',
            'database': 'mineria_de_datos',
            'raise_on_warnings': True
        }

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            raise Exception(err.errno)

        return self.cnx

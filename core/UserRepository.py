import core.MySqlConnection as MySqlConnection


class UserRepository(object):
    def __init__(self):
        self.mySqlConnector = MySqlConnection.MySQLConnector()

    def login(self, userName, password):
        sql = ("SELECT * FROM users u WHERE user_name = %s AND password  = %s ;")
        cnx = self.mySqlConnector.connect()
        cursor = cnx.cursor()
        cursor.execute(sql, (userName, password))
        row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return row

import mysql.connector


class MySql:
    def __init__(self):
        # Mysql server configuration, has to be changed based on individuals credentials
        self.myConnect = mysql.connector.connect(host="localhost", user="root", passwd="")
        self.myCursor = self.myConnect.cursor()

    def print_cursor(self, msg):
        print()
        print(msg)
        for x in self.myCursor:
            print(x)


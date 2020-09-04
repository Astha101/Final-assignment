import mysql.connector

class My_Db:
    def __init__(self):
        self.con = mysql.connector.connect(host="localhost", user="root", password="Asthaupa123", database="epm")
        self.cur = self.con.cursor()
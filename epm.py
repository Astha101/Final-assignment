from Connection import My_Db


class Product(My_Db):
    def __init__(self):
        super().__init__()

    def login_function(self, email, password):
        try:
            qry = ("select * from reg where email=%s and password=%s")
            values = (email, password)
            self.cur.execute(qry, values)
            data = self.cur.fetchone()
            self.con.close()
            return data
        except Exception as es:
            print(es)

    def register_data(self,f_name,l_name,contact,email,password):
        try:
            qry = "INSERT INTO reg (f_name,l_name,contact,email,password)" \
                  " VALUES (%s,%s,%s,%s,%s)"
            values = (f_name,l_name,contact,email,password)
            self.cur.execute(qry, values)
            self.con.commit()
            return True
        except Exception as es:
            print(es)

    def add_product(self, id, type, name, price, qty, payment, delivery):
        try:
            qry = "INSERT INTO product (id, type, name, price, qty, payment, delivery)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (id, type, name, price, qty, payment, delivery)
            self.cur.execute(qry, values)
            self.con.commit()
            return True
        except Exception as es:
            print(es)
            return False

    def update_details(self, id, name, type, price, qty, payment, delivery):
        try:
            qry = "Update product set type=%s,name=%s,price=%s,qty=%s,payment=%s,delivery=%s where id=%s"
            values = (id, name, type, price, qty, payment, delivery)
            self.cur.execute(qry, values)
            self.con.commit()
            return True
        except Exception as es:
            print(es)

    def fetch_data(self):
        try:
            qry = 'select * from product order by name'
            self.cur.execute(qry)
            data = self.cur.fetchall()
            self.con.close()
            return data
        except Exception as es:
            print(es)

    def delete_data(self,id):
        try:
            qry = 'delete from product where id=%s'
            values = (id,)
            self.cur.execute(qry, values)
            self.con.commit()
            self.con.close()
            return True
        except Exception as es:
            print(es)

    def search_data(self, search_by, search):
        try:
            qry = ("select * from product where " + search_by + "  like '" + search + "%' ")
            self.cur.execute(qry)

            data = self.cur.fetchall()
            return data
        except Exception as es:
            print(es)


ob = Product()

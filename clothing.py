import tkinter
from tkinter import *
from tkinter import ttk, filedialog
import mysql.connector
import math
from tkinter import messagebox
import pandas
import sorting

import epm


class Product:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage")
        self.root.geometry("1350x800+350+0")
        self.root.config(bg="cadet blue")
        self.title = Label(self.root, text="Welcome", bd=10, relief=RIDGE, font=("times new roman", 40, 'bold'),
                           bg="#074463", fg="gold")
        self.title.pack(side=TOP, fill=X)
        ############# All Variables ##########
        self.id_var = IntVar()
        self.type_var = StringVar()
        self.name_var = StringVar()
        self.price_var = StringVar()
        self.qty_var = StringVar()
        self.payment_var = StringVar()
        self.delivery_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        ###################### Manage Frame ##########################
        self.Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#074463")
        self.Manage_Frame.place(x=20, y=110, width=475, height=680)

        self.title = Label(self.Manage_Frame, text="Fill Here", bg="#074463", fg="gold",
                           font=("times new roman", 20, "bold"))
        self.title.grid(row=0, columnspan=2, pady=20)
        self.id = Label(self.Manage_Frame, text="Product Id", bg="#074463", fg="gold",
                        font=("times new roman", 15, "bold"))
        self.id.grid(row=1, column=0, padx=20, pady=10, sticky="w")
        self.txt_id = Entry(self.Manage_Frame, textvariable=self.id_var, font=("times new roman", 12, "bold"), bd=5,
                            relief=GROOVE,state="readonly")
        self.txt_id.grid(row=1, column=1, pady=10, padx=10, sticky="w")
        self.type = Label(self.Manage_Frame, text="Product Type", bg="#074463", fg="gold",
                          font=("times new roman", 15, "bold"))
        self.type.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.combo_type = ttk.Combobox(self.Manage_Frame, textvariable=self.type_var,
                                       font=("times new roman", 11, 'bold'),
                                       state='readonly')
        self.combo_type['values'] = ("Cosmetics", "Essentials", "Food")
        self.combo_type.grid(row=2, column=1, padx=10, pady=10)
        self.name = Label(self.Manage_Frame, text="Product Name", bg="#074463", fg="gold",
                          font=("times new roman", 15, "bold"))
        self.name.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.txt_name = Entry(self.Manage_Frame, textvariable=self.name_var, font=("times new roman", 12, "bold"), bd=5,
                              relief=GROOVE)
        self.txt_name.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        self.price = Label(self.Manage_Frame, text="Price", bg="#074463", fg="gold",
                           font=("times new roman", 15, "bold"))
        self.price.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.txt_price = Entry(self.Manage_Frame, textvariable=self.price_var, font=("times new roman", 12, "bold"),
                               bd=5, relief=GROOVE)
        self.txt_price.grid(row=4, column=1, pady=10, padx=10, sticky="w")
        self.qty = Label(self.Manage_Frame, text="Quantity", bg="#074463", fg="gold",
                         font=("times new roman", 15, "bold"))
        self.qty.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        self.txt_qty = Entry(self.Manage_Frame, textvariable=self.qty_var, font=("times new roman", 12, "bold"), bd=5,
                             relief=GROOVE)
        self.txt_qty.grid(row=5, column=1, pady=10, padx=10, sticky="w")
        self.payment = Label(self.Manage_Frame, text="Payment Method", bg="#074463", fg="gold",
                             font=("times new roman", 15, "bold"))
        self.payment.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        self.combo_payment = ttk.Combobox(self.Manage_Frame, textvariable=self.payment_var,
                                          font=("times new roman", 11, 'bold'),
                                          state='readonly')
        self.combo_payment['values'] = ("IMEpay", "Khalti", "ipay", "esewa", "cash on delivery")
        self.combo_payment.grid(row=6, column=1, padx=10, pady=10)
        self.delivery = Label(self.Manage_Frame, text="Deliver To", bg="#074463", fg="gold",
                              font=("times new roman", 15, "bold"))
        self.delivery.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        self.txt_delivery = Entry(self.Manage_Frame, textvariable=self.delivery_var,
                                  font=("times new roman", 12, "bold"), bd=5,
                                  relief=GROOVE)
        self.txt_delivery.grid(row=7, column=1, pady=10, padx=10, sticky="w")

        ############### total ##################3
        self.btn_Frame = Frame(self.Manage_Frame, bd=6, relief=RIDGE, bg="cadet blue")
        self.btn_Frame.place(x=10, y=565, width=200, height=100)
        self.genbtn = Button(self.btn_Frame, text='Generate Bill', command=self.bill,
                             font=('times new roman', 12, 'bold'), bd=6,
                             bg="#074463", fg="gold")
        self.genbtn.grid(row=8, column=0, padx=20, pady=20)


        ###################### Detail Frame ##########################
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#074463")
        self.Detail_Frame.place(x=500, y=110, width=830, height=680)
        self.btn_Frame = Frame(self.Detail_Frame, bd=6, relief=RIDGE, bg="cadet blue")
        self.btn_Frame.place(x=10, y=590, width=770)

        self.Addbtn = Button(self.btn_Frame, bg="#074463", text="Add", width=15, bd=6, fg="gold",
                             font=('times new roman', 10, 'bold'), command=self.add_product).grid(row=0, column=0,
                                                                                                  padx=10,
                                                                                                  pady=10)
        self.updatebtn = Button(self.btn_Frame, bg="#074463", text="Update", bd=6, fg="gold", width=15,
                                font=('times new roman', 10, 'bold'), command=self.update_data).grid(row=0, column=1,
                                                                                                     padx=10,
                                                                                                     pady=10)
        self.deletebtn = Button(self.btn_Frame, bg="#074463", text="Delete", bd=6, fg="gold", width=15,
                                font=('times new roman', 10, 'bold'), command=self.delete_data).grid(row=0, column=2,
                                                                                                     padx=10,
                                                                                                     pady=10)
        self.Clearbtn = Button(self.btn_Frame, bg="#074463", text="Clear", bd=6, fg="gold", width=15,
                               font=('times new roman', 10, 'bold'), command=self.clear_data).grid(row=0, column=3,
                                                                                                   padx=10,
                                                                                                   pady=10)
        ########################## Search  ############################
        search = Label(self.Detail_Frame, text="Search By", bg="#074463", fg="gold",
                       font=("times new roman", 15, 'bold'))
        search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(self.Detail_Frame, textvariable=self.search_by,
                                    font=('times new roman', 12, 'bold'), state='readonly')
        combo_search['values'] = ("Type", "Name")
        combo_search.grid(row=0, column=1, padx=10, pady=10)
        txt_Search = Entry(self.Detail_Frame, textvariable=self.search_txt, width=15,
                           font=("times new roman", 13, 'bold'), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20)
        self.searchbtn = Button(self.Detail_Frame, text="Search", width=9, command=self.search_data).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=10)
        self.showallbtn = Button(self.Detail_Frame, text="Show All", width=9, command=self.fetch_data).grid(row=0,
                                                                                                            column=4,
                                                                                                            padx=10,
                                                                                                            pady=20)
        #################### Table Frame ###########
        self.Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="powder blue")
        self.Table_Frame.place(x=10, y=70, width=800, height=500)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.Product_table = ttk.Treeview(self.Table_Frame,
                                          columns=("id", "type", "name", "price", "qty", "payment", "delivery"),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.Product_table.xview)
        self.scroll_y.config(command=self.Product_table.yview)
        self.Product_table.heading("id", text="Product Id")
        self.Product_table.heading("type", text="Product Type")
        self.Product_table.heading("name", text="Product Name")
        self.Product_table.heading("price", text="Price")
        self.Product_table.heading("qty", text="Quantity")
        self.Product_table.heading("payment", text="Payment Method")
        self.Product_table.heading("delivery", text="Deliver To")

        self.Product_table['show'] = 'headings'
        self.Product_table.column("id", width=100)
        self.Product_table.column("type", width=130)
        self.Product_table.column("name", width=120)
        self.Product_table.column("price", width=100)
        self.Product_table.column("qty", width=100)
        self.Product_table.column("payment", width=120)
        self.Product_table.column("delivery", width=120)

        self.Product_table.pack(fill=BOTH, expand=1)
        self.Product_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()

    def add_product(self):
        # Helps to add the products

        try:
            if self.id_var.get() != "" or self.name_var.get() != "" or self.type_var.get() != "" or \
                    self.price_var.get() != "" or self.qty_var.get() != "" or self.payment_var.get() != ""\
                    or self.delivery_var.get() != "":

                if epm.Product().add_product(self.id_var.get(),
                                             self.type_var.get(),
                                             self.name_var.get(),
                                             self.price_var.get(),
                                             self.qty_var.get(),
                                             self.payment_var.get(),
                                             self.delivery_var.get()):
                    messagebox.showinfo("Success", "Record has been inserted")
                    self.fetch_data()
                    self.clear()

            else:
                messagebox.showerror("Error", "All fields are required")

        except Exception as es:
            print(es)

    def fetch_data(self):
     # Helps to fetch data

            self.Product_table.delete(*self.Product_table.get_children())
            info = sorting.sorting_data(epm.Product().fetch_data())

            for i in info:
                self.Product_table.insert("", "end", text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    def clear(self):
        self.id_var.set("")
        self.type_var.set("")
        self.name_var.set("")
        self.price_var.set("")
        self.qty_var.set("")
        self.payment_var.set("")
        self.delivery_var.set("")

    def clear_data(self):
        self.id_var.set("")
        self.type_var.set("")
        self.name_var.set("")
        self.price_var.set("")
        self.qty_var.set("")
        self.payment_var.set("")
        self.delivery_var.set("")

    def get_cursor(self, ev):
        cursor_row = self.Product_table.focus()
        contents = self.Product_table.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.type_var.set(row[1])
        self.name_var.set(row[2])
        self.price_var.set(row[3])
        self.qty_var.set(row[4])
        self.payment_var.set(row[5])
        self.delivery_var.set(row[6])

    def update_data(self):
        # Helps to update data

        try:
            if self.id_var.get() != "" or self.name_var.get() != "" or self.type_var.get() != "" or \
                    self.price_var.get() != "" or self.qty_var.get() != "" or self.payment_var.get() != "" \
                    or self.delivery_var.get() != "":

                if epm.Product().update_details(self.type_var.get(),
                                                self.name_var.get(),
                                                self.price_var.get(),
                                                self.qty_var.get(),
                                                self.payment_var.get(),
                                                self.delivery_var.get(),
                                                self.id_var.get()):
                    messagebox.showinfo("Success", "Info updated successfully")

                    self.fetch_data()
                    self.clear()


            else:
                messagebox.showerror("Error", "All fields are required")
        except Exception as es:
            print(es)

    def delete_data(self):
        # Helps to delete data

        try:
            if self.id_var.get() != "" or self.name_var.get() != "" or self.type_var.get() != "" \
                    or self.price_var.get() != "" or self.qty_var.get() != "" or self.payment_var.get() != "" \
                    or self.delivery_var.get() != "":
                epm.Product().delete_data(self.id_var.get())
                messagebox.showinfo("Success", "Data deleted successfully")
                self.clear()
                self.fetch_data()
            else:
                messagebox.showerror("Error", "Data field is empty")

        except Exception as es:
            print(es)

    def search_data(self):
        # Helps to search data

        try:
            if self.search_txt.get() != '':
                se = epm.Product().search_data(self.search_by.get(), self.search_txt.get())
                if len(se) != 0:
                    self.Product_table.delete(*self.Product_table.get_children())
                    for row in se:
                        self.Product_table.insert('', END, values=row)

                else:
                    messagebox.showerror("No Results", "Invalid product details")

            else:
                messagebox.showerror("Empty", "It cannot be empty")
        except Exception as es:
            print(es)

        #########################

    def bill(self):
        all_orders = self.Product_table.get_children()
        bill_list = []
        total = 0
        tbl = self.Product_table.item(all_orders[0], 'values')[0]
        # tbl = 0
        for i in all_orders:
            order = self.Product_table.item(i, 'values')
            amt = float(order[3]) * float(order[4])
            bill_list.append((order[0], order[1], order[2], order[3], order[4], order[5], order[6], amt))
            total += amt
            # tbl = order[0]
        generate_bill(bill_list, total)

    ################# Generate Bill #######

class generate_bill:
    def __init__(self, bill_list, total):
        self.window = Tk()
        self.window.title("Bill")
        self.window.geometry("836x470")
        self.window.config(bg="cadet blue")
        self.title = Label(self.window, text="Your Bill", bd=10, relief=RIDGE, font=("times new roman", 20, 'bold'),
                           bg="#074463", fg="gold")
        self.title.pack(side=TOP, fill=X)
        self.Table_Frame = Frame(self.window, bd=4, relief=RIDGE, bg="#074463")
        self.Table_Frame.place(x=7, y=65, width=820, height=400)

        self.conbtn = Button(self.Table_Frame, text="Confirm Order", command=self.confirm_order, bd=6, bg="#074463",
                             fg="gold",
                             font=("times new roman", 12, "bold"))
        self.conbtn.grid(row=8, column=0, pady=330)
        ##############
        self.Table_Frame = Frame(self.Table_Frame, bd=4, relief=RIDGE, bg="powder blue")
        self.Table_Frame.place(x=4, y=5, width=800, height=300)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.Product_table = ttk.Treeview(self.Table_Frame,
                                          columns=(
                                              "id", "type", "name", "price", "qty", "payment", "delivery", 'amount'),
                                          xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.Product_table.xview)
        self.scroll_y.config(command=self.Product_table.yview)
        self.Product_table.heading("id", text="Product Id")
        self.Product_table.heading("type", text="Product Type")
        self.Product_table.heading("name", text="Product Name")
        self.Product_table.heading("price", text="Price")
        self.Product_table.heading("qty", text="Quantity")
        self.Product_table.heading("payment", text="Payment Method")
        self.Product_table.heading("delivery", text="Deliver To")
        self.Product_table.heading("amount", text="Amount")
        self.Product_table['show'] = 'headings'
        self.Product_table.column("id", width=90)
        self.Product_table.column("type", width=100)
        self.Product_table.column("name", width=100)
        self.Product_table.column("price", width=100)
        self.Product_table.column("qty", width=60)
        self.Product_table.column("payment", width=100)
        self.Product_table.column("delivery", width=100)
        self.Product_table.column("amount", width=100)
        self.Product_table.pack(fill=BOTH, expand=1)

        for i in bill_list:
            self.Product_table.insert('', 'end', text='', value=i)

        self.Product_table.insert('', 'end', text='', value=('Total', '', '', '',
                                                             '', '', '', 'Rs.' + str(total)))

    def confirm_order(self):
        ob = messagebox.askyesno("Confirm", "Do you want to proceed?")
        if ob > 0:
            ff = filedialog.asksaveasfilename()
            gg = self.Product_table.get_children()
            id, type, name, price, qty, payment, delivery = [], [], [], [], [], [], []
            for i in gg:
                content = self.Product_table.item(i)
                pp = content['values']
                id.append(pp[0]), type.append(pp[1]), name.append(pp[2]), price.append(pp[3]), qty.append(
                    pp[4]), payment.append(pp[5]), delivery.append(pp[6])
            dd = ['Id', "Type", 'Name', 'Price', "Qty", "Payment", "Delivery"]
            df = pandas.DataFrame(list(zip(id, type, name, price, qty, payment, delivery)), columns=dd)
            paths = r'{}.csv'.format(ff)
            df.to_csv(paths, index=False)
            messagebox.showinfo('Success', 'Your order has been placed '.format(paths))

    def fetch_data(self):

        try:
            self.Product_table.delete(*self.Product_table.get_children())
            info = epm.Product().fetch_data()
            for i in info:
                self.Product_table.insert("", "end", text=i[0], values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
        except Exception as es:
            print(es)



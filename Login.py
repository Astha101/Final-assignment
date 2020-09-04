from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

import epm
from clothing import Product


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("900x600+500+50")
        self.root.config(bg='cadet blue')

        self.txt_email_val = StringVar()
        self.txt_password_val = StringVar()


        #####Login Frame

        self.Frame_login = Frame(self.root, bg="light blue", highlightbackground="black", highlightthickness=3)
        self.Frame_login.place(x=160, y=70, height=480, width=600)

        self.title = Label(self.Frame_login, text="Login Here", font=("algerian", 35, "bold"), fg="light pink",
                           bg="black").place(x=90, y=30)
        self.lbl_email = Label(self.Frame_login, text="Email", font=("times new roman", 15, "bold"), fg="black",
                               bg="light blue").place(
            x=90, y=140)
        self.txt_email = Entry(self.Frame_login, font=("times new roman", 15), bg="light pink",
                               textvariable=self.txt_email_val)
        self.txt_email.place(x=90, y=170, width=350, height=35)

        self.lbl_password = Label(self.Frame_login, text="Password", font=("times new roman", 15, "bold"), bd=0,
                                  fg="black", bg="light blue").place(
            x=90, y=210)
        self.txt_password = Entry(self.Frame_login, font=("times new roman", 15), show="*", bg="light pink",
                                  textvariable=self.txt_password_val)
        self.txt_password.place(x=90, y=240, width=350, height=35)

        self.Login_btn = Button(self.root, command=self.login_function, cursor="hand2", text="Login", fg="pink",
                                bg="black", font=("times new roman", 15)).place(x=250, y=370)

        self.forget_btn = Button(self.Frame_login, text="Dont have an account?", cursor="hand2", fg="black",
                                 bg="light blue", bd=0,
                                 font=("times new roman", 12, "bold")).place(x=80, y=410)

        self.reg_btn = Button(self.Frame_login, text="Register Here", command=self.register_window, fg="light pink",
                              cursor="hand2", bg="black", font=("times new roman", 15)).place(x=300, y=400)

        self.reset_btn = Button(self.root, command=self.ireset, cursor="hand2", text="Reset", fg="pink", bg="black",
                                font=("times new roman", 15)).place(x=360, y=370)

    def register_window(self):
        self.root.destroy()
        import Register

    def login_function(self):

        reg = epm.Product().login_function(self.txt_email_val.get(), self.txt_password_val.get())
        if reg:
            messagebox.showinfo("Success", "Welcome", parent=self.root)
            self.root.destroy()
            root = Tk()
            ob = Product(root)

            import clothing

    def ireset(self):
        """Helps to clear the box"""

        user = (self.txt_email.get())
        password = (self.txt_password.get())
        self.txt_email_val.set("")
        self.txt_password_val.set("")


root = Tk()
obj = Login(root)
root.mainloop()

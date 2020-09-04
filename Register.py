from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

import epm


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("800x900+600+0")
        self.root.config(bg="cadet blue")

        ##### Register Frame ####

        self.frame1 = Frame(self.root, bg="light blue", highlightbackground="black", highlightthickness=3)

        self.frame1.place(x=100, y=130, width=600, height=650)

        self.title = Label(self.frame1, text="Register Here", font=("algerian", 30, "bold"), bg="light blue",
                           fg='black').place(x=50, y=15)

        ########################## rows ###########################

        self.f_name = Label(self.frame1, text="First Name", font=("times new roman", 14, "bold"), bg="light blue",
                            fg='black').place(
            x=80, y=130)
        self.txt_fname = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_fname.place(x=290, y=130)

        self.l_name = Label(self.frame1, text="Last Name", font=("times new roman", 14, "bold"), bg="light blue",
                            fg='black').place(
            x=80, y=180)
        self.txt_lname = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_lname.place(x=290, y=180)

        ####################

        self.contact = Label(self.frame1, text="Contact No.", font=("times new roman", 14, "bold"), bg="light blue",
                             fg='black').place(
            x=80, y=230)
        self.txt_contact = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_contact.place(x=290, y=230)

        self.email = Label(self.frame1, text="Email", font=("times new roman", 14, "bold"), bg="light blue",
                           fg='black').place(
            x=80, y=280)
        self.txt_email = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_email.place(x=290, y=280)

        #########

        self.Password = Label(self.frame1, text="Password", font=("times new roman", 14, "bold"), bg="light blue",
                              fg='black').place(
            x=80, y=330)
        self.txt_password = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_password.place(x=290, y=330)

        self.cpssword = Label(self.frame1, text="Confirm Password", font=("times new roman", 14, "bold"),
                              bg="light blue", fg='black').place(
            x=80, y=380)
        self.txt_cpassword = Entry(self.frame1, font=("times new roman", 14, "bold"), bg="light pink")
        self.txt_cpassword.place(x=290, y=380)

        ######Terms

        self.var_chk = IntVar()
        self.chk = Checkbutton(self.frame1, text="I Agree the Terms & Conditions", variable=self.var_chk, onvalue=1,
                               offvalue=0, bg="light blue", cursor="hand2",
                               font=("times new roman", 12)).place(x=80, y=430)

        self.btn_register = Button(self.frame1, text="Register", font=("times new roman", 12, "bold"), cursor="hand2",
                                   command=self.register_data, bg="light blue", fg="black").place(
            x=80, y=480)

        self.acc_btn = Button(self.frame1, text="Already Have an Account?", bg="light blue", bd="0", fg="black",
                              font=("times new roman", 12)).place(x=80, y=560)

        self.btn_login = Button(self.frame1, text="Sign In", command=self.login_window,
                                font=("times new roman", 12, "bold"), bg="light blue", fg="black").place(x=320, y=560)

    def login_window(self):
        self.root.destroy()
        import Login

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)

    def register_data(self):
        try:
            if(self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_lname.get()=="" or
                    self.txt_contact.get()=="" or
                    self.txt_password.get()=="" or self.txt_cpassword.get()==""):
                messagebox.showerror("Error", "All Fields Are Required",parent=self.root)

            elif self.txt_password.get() != self.txt_cpassword.get():
                messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
            elif self.var_chk.get() == 0:
                messagebox.showerror("Error", "Please agree to the terms and conditions first", parent=self.root)

            if epm.Product().register_data(self.txt_fname.get(),
                                           self.txt_lname.get(),
                                           self.txt_contact.get(),
                                           self.txt_email.get(),
                                           self.txt_password.get()):
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                self.clear()
                self.root.destroy()
                import Login

        except Exception as es:
            print(es)


root = Tk()
obj = Register(root)
root.mainloop()

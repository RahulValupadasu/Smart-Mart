import tkinter as tk
from tkinter import ttk, messagebox
from MySql import MySql

class Login(tk.Frame):
    # below is the __init__ function, which has parent, which represents the parent widget of current object. That is,
    # we are basically sending container which we configured in App and the controller here as the controller acts as
    # common point of interaction between widgets designed
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Below is the code for all the individual frames designed inside Login widget
        self.individual_billing_title_frame = ttk.Frame(self)
        self.login_frame = ttk.Frame(self)
        self.login_frame_pwd = ttk.Frame(self)
        self.button_frame_three = ttk.Frame(self)
        # Below code is for creating the label and text box(entry), for the respective frame and packing it for display
        # All the code below is for various labels, text boxes, buttons. Creating and packing for display on screen
        self.title_label = ttk.Label(self.individual_billing_title_frame, text='Please login to continue', anchor='w',font=('bold'))
        self.title_label.pack(side='left')

        self.login_label = ttk.Label(self.login_frame, width=22, text='LOGIN ID :', anchor='w')
        self.login_entry = ttk.Entry(self.login_frame, width=22)
        self.login_label.pack(side='left')
        self.login_entry.pack(side='left')

        self.login_pwd_label = ttk.Label(self.login_frame_pwd, width=22, text='PASSWORD :', anchor='w')
        self.login_pwd_entry = ttk.Entry(self.login_frame_pwd, show="*", width=22)
        self.login_pwd_label.pack(side='left')
        self.login_pwd_entry.pack(side='left')
        # calling the show_frame function to change the window as per user action
        # self.login_button = ttk.Button(self.button_frame_three, text='Login', command=lambda: controller.show_frame("HomePage"))
        self.login_button = ttk.Button(self.button_frame_three, text='Login', command=lambda: self.login(controller))
        self.quit_button = ttk.Button(self.button_frame_three, text='Exit', command=lambda: controller.exit_window())
        self.login_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=5, pady=5)

        # Packing all the frames to show then with proper layout
        self.individual_billing_title_frame.pack()
        self.login_frame.pack(padx=5, pady=5)
        self.login_frame_pwd.pack(padx=5, pady=5)
        self.button_frame_three.pack(side="bottom", padx=5, pady=5)

    def login(self, controller):
        # inputs from user
        login_value = self.login_entry.get()
        login_pwd = self.login_pwd_entry.get()
        if login_value == "" or login_pwd == "":
            messagebox.showinfo(title="Message", message="Please enter all fields")
        else:
            try:
                # print("::::::try")
                flag = 0
                obj = MySql()
                obj.myCursor.execute("USE PROJECT")
                # checking whether the user exixts or not
                obj.myCursor.execute("SELECT * FROM login WHERE login_id="+login_value+" AND password = "+login_pwd)
                # print(obj.myCursor.arraysize)
                for x in obj.myCursor:
                    flag = flag+1
                    # print(x)
                # print(flag)
                if flag > 0:
                    # if user exists, then we will send him to home page
                    controller.show_frame("HomePage")
                else:
                    messagebox.showinfo(title="Message", message="Login failed, please check credentials")
            except Exception as ex:
                print(str(ex))
                messagebox.showinfo(title="Message", message="Login failed, please check credentials")
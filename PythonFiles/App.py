import tkinter as tk
from IndividualBilling import IndividualBilling
from RegisteringProducts import RegisteringProducts
from ShippingProducts import ShippingProducts
from HomePage import HomePage
from Login import Login
from MySql import MySql


# App class will become the base class inside which we have written code to show other interfaces based on user event
class App(tk.Tk):
    # __init__ function for class App, *args is for more number of arguments sent at once. **kwargs is for key value
    # pairs of more number of arguments
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container and setting the layout, which can change the frames based on user activity
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        # Below mentioned are the list of frames which are called upon with the button press, we are sending the
        # sending the value of new window as string so that there would be new window populated basing on the user event
        self.frames = {"Login": Login(parent=container, controller=self),
                       "HomePage": HomePage(parent=container, controller=self),
                       "RegisteringProducts": RegisteringProducts(parent=container, controller=self),
                       "IndividualBilling": IndividualBilling(parent=container, controller=self),
                       "ShippingProducts": ShippingProducts(parent=container, controller=self)}
        # Aligning the layout of all available frame windows, row=0, column=0 implies they all be on same position
        self.frames["Login"].grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"].grid(row=0, column=0, sticky="nsew")
        self.frames["RegisteringProducts"].grid(row=0, column=0, sticky="nsew")
        self.frames["IndividualBilling"].grid(row=0, column=0, sticky="nsew")
        self.frames["ShippingProducts"].grid(row=0, column=0, sticky="nsew")
        # First window to be shown when user opens app
        self.show_frame("Login")

    # This function below is used to change window frame accordingly, it is called on button click
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # This function below is used to exit the application, it is called on button click, this function is passed to the
    # child class component to exit the main window
    def exit_window(self):
        self.destroy()


# setting the dimension and running the application(This is the main window for application to run)
app = App()
app.title('Smart-Mart')
app.geometry('350x350')
app.mainloop()

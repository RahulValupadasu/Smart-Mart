import tkinter as tk
from tkinter import ttk
from SalesReport import call_sales_report
from StockingReport import call_stocking_report


def show_sales_report():
    call_sales_report()


def show_stocking_report():
    call_stocking_report()


class HomePage(tk.Frame):
    # below is the __init__ function, which has parent, which represents the parent widget of current object. That is
    # we are basically sending container which we configured in App and the controller here as the controller acts as
    # common point of interaction between widgets designed
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Below is the code for all the individual frames designed inside HomePage widget
        self.registering_products_title_frame = ttk.Frame(self)
        self.button_frame_one = ttk.Frame(self)
        self.button_frame_two = ttk.Frame(self)
        self.button_frame_three = ttk.Frame(self)
        # Below code is for creating the label and text box(entry), for the respective frame and packing it for display
        # All the code below is for various labels, text boxes, buttons. Creating and packing for display on screen
        self.title_label = ttk.Label(self.registering_products_title_frame, text='Welcome to the Application!!', anchor='w',  font=('bold'))
        self.title_label.pack(side='left')

        # calling the show_frame function to change the window as per user action
        self.registering_products_btn = ttk.Button(self.button_frame_one, width=100, text="Registering Products", command=lambda: controller.show_frame("RegisteringProducts"))
        self.individual_billing_btn = ttk.Button(self.button_frame_one, width=100, text="Individual Billing", command=lambda: controller.show_frame("IndividualBilling"))
        self.shipping_products_btn = ttk.Button(self.button_frame_one, width=100, text="Shipping Products", command=lambda: controller.show_frame("ShippingProducts"))
        self.registering_products_btn.pack(padx=5, pady=5, )
        self.individual_billing_btn.pack(padx=5, pady=5)
        self.shipping_products_btn.pack(padx=5, pady=5)

        # These buttons will open the report. These are imported, and shown when clicked
        self.sales_report_btn = ttk.Button(self.button_frame_two, text="Sales Report", command=show_sales_report, width=20)
        self.stocking_report_btn = ttk.Button(self.button_frame_two, text="Stocking Report", command=show_stocking_report, width=20)
        self.sales_report_btn.pack(side='left', padx=5, pady=5)
        self.stocking_report_btn.pack(side='left', padx=5, pady=5)

        # These buttons will invoke functions when clicked on then, which opens new window based on function
        # written or may exit the application
        self.logout_button = ttk.Button(self.button_frame_three, text='Log out', command=lambda: controller.show_frame("Login"))
        self.quit_button = ttk.Button(self.button_frame_three, text='Exit', command=lambda: controller.exit_window())
        self.logout_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=5, pady=5)

        # Packing all the frames to show then with proper layout
        self.registering_products_title_frame.pack()
        self.button_frame_one.pack(padx=5, pady=5)
        self.button_frame_two.pack(padx=20, pady=20)
        self.button_frame_three.pack(side="bottom", padx=5, pady=5)

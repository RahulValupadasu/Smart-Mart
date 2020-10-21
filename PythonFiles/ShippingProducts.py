import tkinter as tk
from tkinter import ttk, messagebox
from MySql import MySql


class ShippingProducts(tk.Frame):
    # below is the __init__ function, which has parent, which represents the parent widget of current object. That is
    # we are basically sending container which we configured in App and the controller here as the controller acts as
    # common point of interaction between widgets designed
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Below is the code for all the individual frames designed inside RegisteringProducts widget
        self.shipping_products_title_frame = ttk.Frame(self)
        self.product_number_frame = ttk.Frame(self)
        self.product_units_frame = ttk.Frame(self)
        self.whole_sale_price_frame = ttk.Frame(self)
        self.expiry_date_frame = ttk.Frame(self)
        self.button_frame_three = ttk.Frame(self)
        # Below code is for creating the label and text box(entry), for the respective frame and packing it for display
        # All the code below is for various labels, text boxes, buttons. Creating and packing for display on screen
        self.title_label = ttk.Label(self.shipping_products_title_frame, text='Shipping Products', anchor='w',
                                     font=('bold'))
        self.title_label.pack(side='left')

        self.product_number_label = ttk.Label(self.product_number_frame, width=22, text='Product Number:', anchor='w')
        self.product_number_entry = ttk.Entry(self.product_number_frame, width=22)
        self.product_number_label.pack(side='left')
        self.product_number_entry.pack(side='left')

        self.product_units_label = ttk.Label(self.product_units_frame, width=22, text='Product Units:', anchor='w')
        self.product_units_entry = ttk.Entry(self.product_units_frame, width=22)
        self.product_units_label.pack(side='left')
        self.product_units_entry.pack(side='left')

        self.whole_sale_price_label = ttk.Label(self.whole_sale_price_frame, width=22, text='Product wholesale Price:',
                                                anchor='w')
        self.whole_sale_price_entry = ttk.Entry(self.whole_sale_price_frame, width=22)
        self.whole_sale_price_label.pack(side='left')
        self.whole_sale_price_entry.pack(side='left')

        self.expiry_date_label = ttk.Label(self.expiry_date_frame, width=22, text='Product Expiry Date:', anchor='w')
        self.expiry_date_entry = ttk.Entry(self.expiry_date_frame, width=22)
        self.expiry_date_label.pack(side='left')
        self.expiry_date_entry.pack(side='left')

        # calling the show_frame function to change the window as per user action
        # These buttons will invoke functions when clicked on then, which opens new window based on function
        # written or may exit the application
        self.back_button = ttk.Button(self.button_frame_three, text='Back',
                                      command=lambda: controller.show_frame("HomePage"))
        self.reg_button = ttk.Button(self.button_frame_three, text='Submit', command=self.register_product_to_store)
        self.quit_button = ttk.Button(self.button_frame_three, text='Exit', command=lambda: controller.exit_window())
        self.back_button.pack(side='left', padx=5, pady=5)
        self.reg_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=5, pady=5)

        # Packing all the frames to show then with proper layout
        self.shipping_products_title_frame.pack()
        self.product_number_frame.pack(padx=5, pady=5)
        self.product_units_frame.pack(padx=5, pady=5)
        self.whole_sale_price_frame.pack(padx=5, pady=5)
        self.product_units_frame.pack(padx=5, pady=5)
        self.expiry_date_frame.pack(padx=5, pady=5)
        self.button_frame_three.pack(side="bottom", padx=5, pady=5)

    # function to register products to store, which we will consider for billing
    def register_product_to_store(self, flag=0):
        product_num = self.product_number_entry.get()
        product_units = self.product_units_entry.get()
        product_whole_sale_price = self.whole_sale_price_entry.get()
        product_expiry_date = self.expiry_date_entry.get()
        if product_num == "" or product_units == "" or product_whole_sale_price == "" or product_expiry_date == "":
            messagebox.showinfo(title="Message", message="Please enter all fields")
        else:
            try:
                product_units = float(product_units)
                product_whole_sale_price = float(product_whole_sale_price)
                try:
                    # print("::::::try")
                    product_units = str(product_units)
                    product_whole_sale_price = str(product_whole_sale_price)
                    obj = MySql()
                    obj.myCursor.execute("USE PROJECT")
                    obj.myCursor.execute("SELECT EXISTS(SELECT * from products WHERE product_number='" + product_num + "')")
                    # print("SELECT EXISTS(SELECT * from products WHERE product_name='" + product_num + "')")
                    for x in obj.myCursor:
                        # print(x)
                        if str(x).find("1") != -1:
                            flag = 1
                    if flag == 1:
                        # print(flag)
                        # print("INSERT INTO product_store(product_number, number_of_units, "
                        #                      "product_wholesale_price, "
                        #                      "product_expiry_date) VALUES ('"+product_num+"','" + product_units + "','" + product_whole_sale_price + "','" + product_expiry_date + "')")
                        obj.myCursor.execute("USE PROJECT")
                        obj.myCursor.execute("INSERT INTO product_store(product_number, number_of_units, "
                                             "product_wholesale_price, "
                                             "product_expiry_date) VALUES ('"+product_num+"','" + product_units + "','" + product_whole_sale_price + "','" + product_expiry_date + "')")
                        # emptying the fields after execution
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                        self.whole_sale_price_entry.delete(0, tk.END)
                        self.expiry_date_entry.delete(0,tk.END)
                        obj.myConnect.commit()
                        messagebox.showinfo(title="Message", message="Product added successfully")
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                        self.whole_sale_price_entry.delete(0, tk.END)
                        self.expiry_date_entry.delete(0, tk.END)
                    else:
                        messagebox.showinfo(title="Message", message="Product number does not exist")
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                        self.whole_sale_price_entry.delete(0, tk.END)
                        self.expiry_date_entry.delete(0, tk.END)
                except Exception as ex:
                    print(str(ex))
                    obj.myConnect.rollback()
                    if str(ex).find("Duplicate entry") != -1:
                        messagebox.showinfo(title="Message",
                                            message="Product with product number " + product_num + " already exists")
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                        self.whole_sale_price_entry.delete(0, tk.END)
                        self.expiry_date_entry.delete(0, tk.END)
                    else:
                        messagebox.showinfo(title="Message", message="Something went wrong")
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                        self.whole_sale_price_entry.delete(0, tk.END)
                        self.expiry_date_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showinfo(title="Message", message="Please enter an numeric value for product units and whole sale price")
                self.product_number_entry.delete(0, tk.END)
                self.product_units_entry.delete(0, tk.END)
                self.whole_sale_price_entry.delete(0, tk.END)
                self.expiry_date_entry.delete(0, tk.END)

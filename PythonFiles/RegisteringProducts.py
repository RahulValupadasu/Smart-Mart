import tkinter as tk
from tkinter import ttk, messagebox
from MySql import MySql


class RegisteringProducts(tk.Frame):
    # below is the __init__ function, which has parent, which represents the parent widget of current object. That is
    # we are basically sending container which we configured in App and the controller here as the controller acts as
    # common point of interaction between widgets designed
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Below is the code for all the individual frames designed inside RegisteringProducts widget
        self.registering_products_title_frame = ttk.Frame(self)
        self.product_number_frame = ttk.Frame(self)
        self.product_name_frame = ttk.Frame(self)
        self.product_description_frame = ttk.Frame(self)
        self.product_unit_price_frame = ttk.Frame(self)
        self.button_frame_three = ttk.Frame(self)
        # Below code is for creating the label and text box(entry), for the respective frame and packing it for display
        # All the code below is for various labels, text boxes, buttons. Creating and packing for display on screen
        self.title_label = ttk.Label(self.registering_products_title_frame, text='Registering products', anchor='w',  font=('bold'))
        self.title_label.pack(side='left')

        self.product_number_label = ttk.Label(self.product_number_frame, width=22, text='Product Number:',anchor='w')
        self.product_number_entry = ttk.Entry(self.product_number_frame, width=22)
        self.product_number_label.pack(side='left')
        self.product_number_entry.pack(side='left')

        self.product_name_label = ttk.Label(self.product_name_frame, width=22, text='Product Name:', anchor='w')
        self.product_name_entry = ttk.Entry(self.product_name_frame, width=22)
        self.product_name_label.pack(side='left')
        self.product_name_entry.pack(side='left')

        self.product_description_label = ttk.Label(self.product_description_frame, width=22,text='Product Description:', anchor='w')
        self.product_description_entry = ttk.Entry(self.product_description_frame, width=22)
        self.product_description_label.pack(side='left')
        self.product_description_entry.pack(side='left')

        self.product_unit_price_frame_label = ttk.Label(self.product_unit_price_frame, width=22, text='Product Unit Price:', anchor='w')
        self.product_unit_price_frame_entry = ttk.Entry(self.product_unit_price_frame, width=22)
        self.product_unit_price_frame_label.pack(side='left')
        self.product_unit_price_frame_entry.pack(side='left')
        # calling the show_frame function to change the window as per user action
        # These buttons will invoke functions when clicked on then, which opens new window based on function
        # written or may exit the application
        self.back_button = ttk.Button(self.button_frame_three, text='Back',  command=lambda: controller.show_frame("HomePage"))
        self.reg_button = ttk.Button(self.button_frame_three, text='Submit', command=self.register_product)
        self.quit_button = ttk.Button(self.button_frame_three, text='Exit', command=lambda: controller.exit_window())
        self.back_button.pack(side='left', padx=5, pady=5)
        self.reg_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=5, pady=5)

        # Packing all the frames to show then with proper layout
        self.registering_products_title_frame.pack()
        self.product_number_frame.pack(padx=5, pady=5)
        self.product_name_frame.pack(padx=5, pady=5)
        self.product_description_frame.pack(padx=5, pady=5)
        self.product_unit_price_frame.pack(padx=5, pady=5)
        self.button_frame_three.pack(side="bottom", padx=5, pady=5)

    # function to store data in the products table in database
    def register_product(self):
        product_num = self.product_number_entry.get()
        product_name = self.product_name_entry.get()
        product_description = self.product_description_entry.get()
        product_unit_price = self.product_unit_price_frame_entry.get()
        if product_num == "" or product_name == "" or product_description == "" or product_unit_price == "":
            messagebox.showinfo(title="Message", message="Please enter all fields")
        else:
            try:
                product_unit_price = float(product_unit_price)
                try:
                    product_unit_price = str(product_unit_price)
                    # print("::::::try")
                    obj = MySql()
                    obj.myCursor.execute("USE PROJECT")
                    # insert query
                    obj.myCursor.execute("INSERT INTO products(product_number, product_name, product_description, "
                                         "product_unit_price) VALUES ('" + product_num + "','" + product_name + "','" + product_description + "','" + product_unit_price + "')")
                    obj.myConnect.commit()
                    messagebox.showinfo(title="Message", message="Product added successfully")
                    self.product_number_entry.delete(0, tk.END)
                    self.product_name_entry.delete(0, tk.END)
                    self.product_description_entry.delete(0, tk.END)
                    self.product_unit_price_frame_entry.delete(0, tk.END)
                except Exception as ex:
                    print(str(ex))
                    obj.myConnect.rollback()
                    if str(ex).find("Duplicate entry") != -1:
                        messagebox.showinfo(title="Message",
                                            message="Product with product number " + product_num + " already exists")
                        # emptying the fields after execution
                        self.product_number_entry.delete(0, tk.END)
                        self.product_name_entry.delete(0, tk.END)
                        self.product_description_entry.delete(0, tk.END)
                        self.product_unit_price_frame_entry.delete(0, tk.END)
                    else:
                        messagebox.showinfo(title="Message", message="Something went wrong")
                        # emptying the fields after execution
                        self.product_number_entry.delete(0, tk.END)
                        self.product_name_entry.delete(0, tk.END)
                        self.product_description_entry.delete(0, tk.END)
                        self.product_unit_price_frame_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showinfo(title="Message", message="Please enter an numeric value for product unit price")
                self.product_number_entry.delete(0, tk.END)
                self.product_name_entry.delete(0, tk.END)
                self.product_description_entry.delete(0, tk.END)
                self.product_unit_price_frame_entry.delete(0, tk.END)

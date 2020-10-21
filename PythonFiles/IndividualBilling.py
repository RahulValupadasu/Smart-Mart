import tkinter as tk
from tkinter import ttk, messagebox
from MySql import MySql


class IndividualBilling(tk.Frame):
    # below is the __init__ function, which has parent, which represents the parent widget of current object. That is
    # we are basically sending container which we configured in App and the controller here as the controller acts as
    # common point of interaction between widgets designed
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.billing_obj_list = []
        self.final_str = ""
        # Below is the code for all the individual frames designed inside IndividualBilling widget
        self.individual_billing_title_frame = ttk.Frame(self)
        self.product_number_frame = ttk.Frame(self)
        self.product_units_frame = ttk.Frame(self)
        self.button_frame_three = ttk.Frame(self)
        self.button_frame_four = ttk.Frame(self)
        # Below code is for creating the label and text box(entry), for the respective frame and packing it for display
        # All the code below is for various labels, text boxes, buttons. Creating and packing for display on screen
        self.title_label = ttk.Label(self.individual_billing_title_frame, text='Individual Billing', anchor='w',
                                     font=('bold'))
        self.title_label.pack(side='left')

        self.product_number_label = ttk.Label(self.product_number_frame, width=22, text='Product Number:', anchor='w')
        self.product_number_entry = ttk.Entry(self.product_number_frame, width=22)
        self.product_number_label.pack(side='left')
        self.product_number_entry.pack(side='left')

        self.product_units_label = ttk.Label(self.product_units_frame, width=22, text='Number Of Units:', anchor='w')
        self.product_units_entry = ttk.Entry(self.product_units_frame, width=22)
        self.product_units_label.pack(side='left')
        self.product_units_entry.pack(side='left')

        self.generate_bill = ttk.Button(self.button_frame_four, text='Generate Bill', command=self.confirm_bill)
        self.add_more = ttk.Button(self.button_frame_four, text='Submit and Add More', command=self.submit_and_add_more)
        self.generate_bill.pack(side='left', padx=5, pady=5)
        self.add_more.pack(side='left', padx=5, pady=5)

        # calling the show_frame function to change the window as per user action
        # These buttons will invoke functions when clicked on then, which opens new window based on function
        # written or may exit the application
        # self.back_button = ttk.Button(self.button_frame_three, text='Back',command=lambda: controller.show_frame("HomePage"))
        self.back_button = ttk.Button(self.button_frame_three, text='Back',
                                      command=lambda: self.landing_window(controller))
        self.reg_button = ttk.Button(self.button_frame_three, text='Submit')
        self.quit_button = ttk.Button(self.button_frame_three, text='Exit', command=lambda: controller.exit_window())
        self.back_button.pack(side='left', padx=5, pady=5)
        self.reg_button.pack(side='left', padx=5, pady=5)
        self.quit_button.pack(side='left', padx=5, pady=5)

        # Packing all the frames to show then with proper layout
        self.individual_billing_title_frame.pack()
        self.product_number_frame.pack(padx=5, pady=5)
        self.product_units_frame.pack(padx=5, pady=5)
        self.button_frame_four.pack(padx=5, pady=5)
        self.button_frame_three.pack(side="bottom", padx=5, pady=5)

    def landing_window(self, controller):
        controller.show_frame("HomePage")
        self.final_str = ""
        self.billing_obj_list = []

    # will take inputs from user repeatedly and push the data into a list
    def submit_and_add_more(self, flag=0):
        # user inputs
        product_num = self.product_number_entry.get()
        product_units = self.product_units_entry.get()
        # validations
        if product_num == "" or product_units == "":
            messagebox.showinfo(title="Message", message="Please enter all fields")
        else:
            try:
                # making sure product_units are numeric
                product_units = float(product_units)
                try:
                    obj = MySql()
                    obj.myCursor.execute("USE PROJECT")
                    # checking whether the product with product_number exists or not
                    obj.myCursor.execute(
                        "SELECT EXISTS(SELECT * from products WHERE product_number='" + product_num + "')")
                    for x in obj.myCursor:
                        if str(x).find("1") != -1:
                            flag = 1
                    if flag == 1:
                        # checking the stock of the product to proceed further
                        obj.myCursor.execute("USE PROJECT")
                        obj.myCursor.execute("SELECT (sb.number_of_units-sb.sold_units) AS number_units_available "
                                             "FROM (SELECT product_store.product_number, products.product_name ,"
                                             "product_store.number_of_units , COALESCE(sum("
                                             "store_products_billing.quantity),0) AS "
                                             "sold_units FROM product_store LEFT JOIN store_products_billing ON "
                                             "store_products_billing.product_number = product_store.product_number "
                                             "LEFT JOIN products ON products.product_number = "
                                             "product_store.product_number GROUP BY product_store.product_number, "
                                             "product_store.number_of_units) sb WHERE sb.product_number = "
                                             "'" + product_num + "'")
                        for x in obj.myCursor.fetchall():
                            stock = x[0]
                            break
                        # if stock < product_units and stock-product_units != 1: messagebox.showinfo(title="Message",
                        # message="Not enough stock available, Available stock is: "+str(stock)) else:
                        flag = product_units
                        for x in self.billing_obj_list:
                            if x[0] == product_num:
                                flag = flag + x[1]
                        # print(flag)
                        # print(stock)
                        # print(product_units)
                        # if stock is there then only the product can be sold
                        if flag <= stock:
                            obj.myCursor.execute(
                                "SELECT product_unit_price FROM products WHERE product_number = '" + product_num + "'")
                            records = obj.myCursor.fetchall()
                            product_unit_price_from_db = [record[0] for record in records][0]
                            individual_list = [product_num, product_units, product_unit_price_from_db]
                            # individual object will be appended to list, to maintain the bill chain
                            self.billing_obj_list.append(individual_list)
                            # emptying the fields after execution
                            self.product_number_entry.delete(0, tk.END)
                            self.product_units_entry.delete(0, tk.END)
                            self.final_str = self.final_str + "Product Number: " + str(
                                product_num) + "\nProduct Units: " + str(product_units) + "\nUnit Price: " + str(
                                product_unit_price_from_db) + "\nPrice: " + str(
                                float(product_units) * float(product_unit_price_from_db)) + "\n\n"
                            messagebox.showinfo(title="Message",
                                                message=self.final_str + "\n\nProceed to add other item ("
                                                                         "or) generate bill")
                        else:
                            messagebox.showinfo(title="Message",
                                                message="Not enough stock available, as you added products with "
                                                        "same product number, Now Available: " + str(
                                                    product_units + stock - flag))
                    else:
                        messagebox.showinfo(title="Message", message="Product number does not exist")
                        # emptying the fields after execution
                        self.product_number_entry.delete(0, tk.END)
                        self.product_units_entry.delete(0, tk.END)
                except Exception as ex:
                    # print(str(ex))
                    messagebox.showinfo(title="Message", message="Something went wrong")
                    self.product_number_entry.delete(0, tk.END)
                    self.product_units_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showinfo(title="Message",
                                    message="Please enter an numeric value for product units")
                self.product_number_entry.delete(0, tk.END)
                self.product_units_entry.delete(0, tk.END)

    # The list of all objects will be inserted using executemany statement
    def confirm_bill(self):
        if len(self.billing_obj_list) > 0:
            try:
                total_bill_amount = 0
                for x in self.billing_obj_list:
                    bill_amount = float(x[1]) * float(x[2])
                    total_bill_amount = total_bill_amount + bill_amount
                stmt_one = "INSERT INTO billing (amount, total_amount) VALUES ('" + str(
                    total_bill_amount) + "', '" + str(total_bill_amount + (total_bill_amount * 0.13)) + "')"
                obj = MySql()
                obj.myCursor.execute("USE PROJECT")
                obj.myCursor.execute(stmt_one)
                last_inserted = obj.myCursor.lastrowid
                for x in self.billing_obj_list:
                    x.insert(0, last_inserted)
                stmt_two = "INSERT INTO store_products_billing (billing_id, product_number, quantity, price) VALUES (%s, %s, %s, %s)"
                obj.myCursor.executemany(stmt_two, self.billing_obj_list)
                self.product_number_entry.delete(0, tk.END)
                self.product_units_entry.delete(0, tk.END)
                obj.myConnect.commit()
                messagebox.showinfo(title="Message", message=self.final_str + "\nTotal: " + str(
                    total_bill_amount) + "\nTax(13%): " + str(total_bill_amount * 0.13) + "\nNet Total: " + str(
                    total_bill_amount + (total_bill_amount * 0.13)) + "\n\nBill successfully generated")
                self.final_str = ""
                self.billing_obj_list = []
            except Exception as ex:
                print(str(ex))
                obj.myConnect.rollback()
                messagebox.showinfo(title="Message", message="Something went wrong")
                self.product_number_entry.delete(0, tk.END)
                self.product_units_entry.delete(0, tk.END)
        else:
            messagebox.showinfo(title="Message",
                                message="Please use 'Submit and Add More' button to add items to bill one by one, "
                                        "before generating final bill")

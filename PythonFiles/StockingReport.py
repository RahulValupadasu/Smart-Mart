from tkinter import *
from tkinter import messagebox

from MySql import MySql


class StockingReport:
    # This is the init function of this SalesReports class
    def __init__(self, tab):
        try:
            obj = MySql()
            obj.myCursor.execute("USE PROJECT")
            # query for available stock for each product
            obj.myCursor.execute("SELECT sb.product_number ,sb.product_name,"
                                 "(sb.number_of_units-sb.sold_units) AS number_units_available FROM (SELECT "
                                 "product_store.product_number, products.product_name ,product_store.number_of_units "
                                 ", sum(store_products_billing.quantity) AS sold_units FROM product_store LEFT JOIN "
                                 "store_products_billing ON store_products_billing.product_number = "
                                 "product_store.product_number LEFT JOIN products ON products.product_number = "
                                 "product_store.product_number GROUP BY product_store.product_number, "
                                 "product_store.number_of_units) sb WHERE sb.number_of_units-sb.sold_units < 10")
            columns = [column[0] for column in obj.myCursor.description]
            results = []
            # converting dictionary into list of lists
            for row in obj.myCursor.fetchall():
                results.append(dict(zip(columns, row)))
            self.lst = []
            for row in results:
                row2 = []
                for key in ['product_number', 'product_name', 'number_units_available']:
                    row2.append(row[key])
                self.lst.append(row2)
            if len(self.lst) == 0:
                messagebox.showinfo(title="Message", message="All products are in-stock(every individual product is "
                                                             "available with more than 10 units) so report will be "
                                                             "empty")
            self.lst.insert(0, ['Product Number', 'Product Name', 'Quantity Remaining'])
        except Exception as ex:
            print(str(ex))
        # Setting column and row values to be able to form table
        total_rows = len(self.lst)
        total_columns = len(self.lst[0])
        # creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(tab, width=20)
                self.e.grid(row=i, column=j)
                self.e.insert(END, self.lst[i][j])


# Function to create table using class above, and display
def call_stocking_report():
    tab = Tk()
    t = StockingReport(tab)
    tab.title('Stocking Report')
    tab.mainloop()

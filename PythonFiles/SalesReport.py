from tkinter import *

from MySql import MySql


class SalesReport:
    # This is the init function of this SalesReports class
    def __init__(self, tab):
        try:
            print("::::::try salesReport")
            obj = MySql()
            obj.myCursor.execute("USE PROJECT")
            # Query for generating sales report
            obj.myCursor.execute("SELECT products.product_name, sum(store_products_billing.quantity) AS quantity, "
                                 "store_products_billing.price AS unit_price FROM store_products_billing LEFT JOIN "
                                 "products ON store_products_billing.product_number = products.product_number GROUP "
                                 "BY products.product_name, store_products_billing.price")
            # print(obj.myCursor.arraysize)
            columns = [column[0] for column in obj.myCursor.description]
            # print(columns)
            results = []
            # converting dictionary into list of lists
            for row in obj.myCursor.fetchall():
                results.append(dict(zip(columns, row)))
            self.lst = []
            for row in results:
                row2 = []
                for key in ['product_name', 'quantity', 'unit_price']:
                    row2.append(row[key])
                self.lst.append(row2)
            total_sum = 0
            for x in self.lst:
                x.append(str(float(x[1])*float(x[2])))
                total_sum = total_sum + float(x[1])*float(x[2])
            self.lst.insert(0, ['Product Name', 'Quantity', 'Unit Price', 'Unit Total'])
            self.lst.append(('', '', 'Total', total_sum))
            self.lst.append(('', '', 'Tax(13%): ', str(round((0.13*total_sum),2))))
            self.lst.append(('', '', 'Net Total: ', str(total_sum + (0.13 * total_sum))))
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
def call_sales_report():
    tab = Tk()
    t = SalesReport(tab)
    tab.title('Sales Report')
    tab.mainloop()


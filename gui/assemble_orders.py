import tkinter
from tkinter import *
from tkinter import messagebox
import random
from class_defs.customer import customer_two as c
from class_defs.invoice import Invoice

class AssembleOrders:
    def __init__(self):
        self.invoice_num = 1001
        self.current = Invoice(self.invoice_num, c)
        self.clicked = StringVar()
        self.clicked.set("Trophy 1")
        self.trophy_list = ["Trophy 1", "Trophy 2", "Trophy 3", "Trophy 4", "Trophy 5", "Trophy 6"]
        self.start_button = tkinter.Button(m, text='Start New Order', width=25, command=self.new_order)
        self.clear_button = tkinter.Button(m, text='Clear Order', width=25, command=self.clear, state=DISABLED)
        self.add_trophy = OptionMenu(m, self.clicked, *self.trophy_list)
        self.add_button = tkinter.Button(m, text='Add to Order', width=25, command=self.add, state=DISABLED)
        self.create_invoice_button = tkinter.Button(m, text='Create Invoice', width=25, command=self.create_invoice, state=DISABLED)

    def new_order(self):
        self.invoice_num += 1
        new_inv = Invoice(self.invoice_num, c)
        self.current = new_inv
        self.add_button['state'] = NORMAL
        self.create_invoice_button['state'] = NORMAL

    def add(self):
        if self.clicked.get() == "Trophy 1":
            self.current.items_with_price.update({'Trophy 1': 9.99})
        elif self.clicked.get() == "Trophy 2":
            self.current.add_item({'Trohpy 2': 10.99})
        elif self.clicked.get() == "Trohpy 3":
            self.current.add_item({'Trohpy 3': 11.99})
        elif self.clicked.get() == "Trohpy 4":
            self.current.add_item({'Trohpy 4': 11.99})
        elif self.clicked.get() == "Trohpy 5":
            self.current.add_item({'Trohpy 5': 12.99})
        elif self.clicked.get() == "Trohpy 6":
            self.current.add_item({'Trohpy 6': 13.99})
        messagebox.showinfo(message="Item added")
        self.clear_button['state'] = NORMAL

    def clear(self):
        self.current.items_with_price.clear()
        messagebox.showinfo(message="Items Cleared")

    def create_invoice(self):
        self.current.create_invoice()


# create main window
m = tkinter.Tk()
m.title('Trophy Orders')

label = tkinter.Label(m, text="Trophy Orders")
label.grid(row=1)

# create an object
session = AssembleOrders()

session.start_button.grid(row=2)

# add trophy function
session.add_trophy.grid(row=3)
label2 = tkinter.Label(m, text=" ")
label2.grid(row=4)

session.add_button.grid(row=5)

#new, clear, and exit

session.clear_button.grid(row=6)
session.create_invoice_button.grid(row=7)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=8)
m.mainloop()

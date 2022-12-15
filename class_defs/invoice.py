from class_defs.customer import Customer as c


class InvalidInvoiceIDException(Exception):
    """InvalidInvoiceIDException is derived class of Exception base class"""
    pass


class Invoice:
    """Invoice Class"""

    # Constructor
    def __init__(self, invID, cust, ip_dict={}):
        id_characters = set("1234567890")
        if not id_characters.issuperset(str(invID)):
            raise InvalidInvoiceIDException
        self.invoice_id = invID
        self.customer = cust
        self.items_with_price = ip_dict

    def __str__(self):
        return self.invoice_id + ": " + self.customer.__str__()

    def __repr__(self):
        return 'invoice({},{},{}'.format(self.invoice_id, self.customer, self.items_with_price)

    def add_item(self, dict):
        self.items_with_price.update(dict)

    def create_invoice(self):
        total = 0
        tax = 0
        print(self.customer.__str__())
        for key, value in self.items_with_price.items():
            print(key, '.....', value)
            total += value
        tax = total * 0.06
        total += tax
        print('Tax..........' + "${:.2f}".format(tax))
        print('Total.....' + "${:.2f}".format(total))

# Driver

#invoice1 = Invoice(1123, c('2999', 'Duck', 'Donald', '(515)555-5555', '123', 'Main', 'Street', 'Small Town', 'IA', '11111'))
#invoice1.add_item({'iPad': 799.99})
#invoice1.add_item({'Surface': 999.99})
#invoice1.create_invoice()
#del invoice1

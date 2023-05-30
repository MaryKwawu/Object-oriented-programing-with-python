from item import Item


class Phone(Item):
    # all = [] we will not need the empty list because of the supper class

    def __init__(self, name, price, quantity=0, broken_phones=0):
        # using the super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        # Run validation to the recieved arguement: assert-it prevents negative values from printing and also catching bugs
        # assert price >= 0, f"Price{price} is not greater than or equal to zero"
        # assert quantity >= 0, f"Quantity{quantity} is not greater or equal to zero"
        # assert broken_phones >= 0, f"broken_phones{broken_phones} is not greater or equal to zero"

    def send_email(self):
        # Implement your email sending logic here
        print(f"Sending email for {self.name}...")

    # creating a self object
    # self.name = name
    # self.price = price
    # self.quantity = quantity
    # self.broken_phones = broken_phones

    # Actions to execute
    # Phone.all.append(self) super class has made up redundant


phone1 = Phone("SamsungPhonev10", 500, 5, 1)
phone1.send_email()
# print(Item.all)
# print(Phone.all)
# print(phone1.calculate_total_price())
# phone1.broken_phones = 1
phone2 = Phone("technoPhonev20", 700, 5, 1)
# phone2.broken_phones = 1

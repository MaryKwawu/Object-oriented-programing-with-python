import csv


class Item:
    pay_rate = 0.8  # this is an attribute for class but it can be accessed by an instance also
    all = []

    def __init__(self, name, price, quantity=0):
        # Run validation to the recieved arguement: assert-it prevents negative values from printing and also catching bugs
        assert price >= 0, f"Price{price} is not greater than or equal to zero"
        assert quantity >= 0;
        f"Quantity{quantity} is not greater or equal equal to zero"

        # creating a self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
        # self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
             # print(item)

    def __repr__(self):
        return f"Item('{self.name}, {self.price}, {self.quantity})"


Item.instantiate_from_csv()
print(Item.all)

# creating an instance of Item
item1 = Item("Phone", 500, 20)
# item2 = Item("Laptop", 1000, 3)
item1.apply_discount()
# print(item1.price)


item2 = Item("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
# print(item2.price)


# print(Item.all)
# for instance in Item.all:
#   print(instance.name)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__) # allows you to see all the attribute of class level
# print(item1.__dict__) # allows you to see all the attribute of instance  level

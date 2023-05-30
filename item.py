import csv


class Item:
    pay_rate = 0.8  # this is an attribute for class but it can be accessed by an instance also
    all = []

    def __init__(self, name:str, price:float, quantity=0):
        # Run validation to the recieved arguement: assert-it prevents negative values from printing and also catching bugs
        assert price >= 0, f"Price{price} is not greater than or equal to zero"
        assert quantity >= 0;f"Quantity{quantity} is not greater or equal equal to zero"

        # creating a self object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

        @property
        def price(self):
            return self.__price

    def apply_discount(self):
        self.price = self.price * self.pay_rate
            # self.price = self.price * self.pay_rate

    def apply_increment(self, increment_value):
           self.price = self.price + self.price * increment_value

        # @property
        # def read_only_name(self):
        #     return "Mary"

    def calculate_total_price(self):
        return self.price * self.quantity


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

    def is_integer(num):
        # counting out floats ie 5.0, 12.0
        if isinstance(num, float):
            # count out float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def is_checking(num):
        # to print out either an integer or a floating number
        if isinstance(num, (int, float)):
            return True
        else:
            return False

    def is_decimal(num):
        # Print out floating numbers
        if isinstance(num, int):
            return False
        elif isinstance(num, float):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity})"

    @property
    # proper Decorator = Read-only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too longooo!")
        else:
            self.__name = value









# print("You are trying to set")


# print(Item.is_checking(5.5))

# Item.instantiate_from_csv()
# print(Item.all)

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


# print(Item.is_checking(5.5))

# Item.instantiate_from_csv()
# print(Item.all)

# creating an instance of Item
# item1 = Item("Phone", 500, 20)
# item2 = Item("Laptop", 1000, 3)
# item1.apply_discount()
# print(item1.price)


# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.all)
# for instance in Item.all:
#   print(instance.name)
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(Item.__dict__) # allows you to see all the attribute of class level
# print(item1.__dict__) # allows you to see all the attribute of instance  level

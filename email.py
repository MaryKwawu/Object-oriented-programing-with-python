import csv
from item import Item


@classmethod
def instantiate_from_csv(cls):
    pass
    # with open('items.csv', 'r') as f:
    #     reader = csv.DictReader(f)
    #     items = list(reader)
    #
    # for item in items:
    #     Item(
    #         name=item.get('name'),
    #         price=float(item.get('price')),
    #         quantity=int(item.get('quantity')),
    #     )


@staticmethod
def is_integer(num):
    pass
    # if isinstance(num, float):
    #     return num.is_integer()
    # elif isinstance(num, int):
    #     return True
    # else:
    #     return False


def __repr__(self):
    def __connect(self, smpt_server):
        pass


def __prepare_body(self):
    return f"""Hello Someone. We have {self.name} {self.quantity} times. Regards, JimShapedCoding"""


def __send(self):
    pass


def send_email(self):
    self.__connect()
    self.__prepare_body()
    self.__send()

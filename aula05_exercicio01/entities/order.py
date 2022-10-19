from datetime import datetime
from entities import OrderItem

class Order:

    def __init__(self):
        self.__moment = datetime.now()
        self.__orders = []

    @property
    def moment(self):
        return self.__moment

    def add_item(self, item):
        self.orders.append(item)

    def remove_item(self, item):
        self.orders.remove(item)

    @property
    def orders(self):
        return self.__orders

    def total(self):
        soma = 0
        for item in orders:
            soma += item.sub_total()
        return soma

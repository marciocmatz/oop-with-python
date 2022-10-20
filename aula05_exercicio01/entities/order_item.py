
class OrderItem:

    def __init__(self, product, quantity, price):
        self.__product = product
        self.__quantity = quantity
        self.__price = price

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def sub_total(self):
        return self.__quantity * self.__price

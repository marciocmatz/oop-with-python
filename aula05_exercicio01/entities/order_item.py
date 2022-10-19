
class OrderItem:

    def __init__(self, quantity, price, product):
        self.__quantity = quantity
        self.__price = price
        self.__product = product

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, new_product):
        self.__product = new_product

    def sub_total(self):
        return f'{(self.__quantity * self.__price):.2f}'

    def __str__(self):
        return f'{self.__product.name} ->> Quantity: {self.__quantity} // SUBTOTAL: {self.sub_total()}'

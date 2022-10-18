
class Product:

    def __init__(self, name=None, price=0.0, quantity=0) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_in_stock(self) -> str:
        return self.price * self.quantity

    def add_products(self, quantity: int) -> None:
        self.quantity += quantity

    def remove_products(self, quantity: int) -> None:
        self.quantity -= quantity

    def __str__(self) -> str:
        return f'Product data: {self.name}, R$ {self.price:.2f}, {self.quantity} units. Total R$ {self.total_value_in_stock():.2f}'

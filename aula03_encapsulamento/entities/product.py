
class Product:
    """
    É preciso entender que Python tem um filosofia diferente de outras linguagens.
    Nem sempre getters e setters são precisos, como é o caso do Java.
    """

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price) -> None:
        self.__price = price


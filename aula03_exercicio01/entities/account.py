class Account:


    def __init__(self, acc_number: int, acc_holder: str, *args):
        self.__acc_number = acc_number
        self.__acc_holder = acc_holder

        if args:
            self.__balance = args[0]

    @property
    def acc_number(self) -> int:
        return self.__acc_number

    @property
    def acc_holder(self) -> str:
        return self.__acc_holder

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, value: float) -> None:
        self.__balance += value

    def withdraw(self, value: float) -> None:
        self.__balance -= (value + 5)

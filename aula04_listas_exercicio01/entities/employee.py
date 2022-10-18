
class Employee:


    def __init__(self, id_funcionario: int, name: str, salary: float) -> None:
        self.__id_funcionario = id_funcionario
        self.__name = name
        self.__salary = salary

    @property
    def id_funcionario(self) -> int:
        return self.__id_funcionario

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def salary(self) -> float:
        return self.__salary

    def increase_salary(self, percentage: float) -> None:
        self.__salary += (self.__salary * percentage / 100)

    def __str__(self) -> str:
        return f'{self.__id_funcionario} -> {self.__name} / Salary R$ {self.__salary:.2f}'


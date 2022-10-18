

class Worker:

    contracts = []

    def __init__(self, name, level, base_salary, department):
        self.__name = name
        self.__level = level
        self.__base_salary = base_salary
        self.__department = department

    @property
    def name(self):
        return self.__name

    @name.setter
    def date(self, new_name):
        self.__name = new_name

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, new_level):
        self.__level = new_level

    @property
    def base_salary(self):
        return self.__base_salary

    @base_salary.setter
    def hours(self, new_base_salary):
        self.__base_salary = new_base_salary

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, new_department):
        self.__department = new_department

    def add_contract(self, contract):
        self.contracts.append(contract)

    def remove_contract(self, contract):
        self.contracts.remove(contract)

    def income(self, year, month):
        soma_total = 0
        for contract in self.contracts:
            if contract.date.year == year and contract.date.month == month:
                soma_total += contract.total_value()
        return soma_total + self.__base_salary

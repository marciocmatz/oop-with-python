
class Employee:

    def __init__(self, name=None, gross_salary=0.0, tax=0.0) -> None:
        self.name = name
        self.gross_salary = gross_salary
        self.tax = tax

    def net_salary(self) -> float:
        return self.gross_salary - self.tax

    def increase_salary(self, percentage: float) -> None:
        self.gross_salary += self.gross_salary * (percentage / 100)

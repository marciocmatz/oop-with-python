from datetime import datetime
from entities import Worker, HourContract, WorkerLevel

department_name = input("Enter department's name: ")

print()
print('Enter worker data:')
name = input('Name: ')
level = input('Level: ')
base_salary = float(input('Base Salary: '))
print()

worker = Worker(name, level, base_salary, department_name)

n = int(input('How many contracts to this worker? '))

for i in range(1, n + 1):
    print()
    print(f'Enter contrat #{i} data:')
    date = datetime.strptime(input('Date (dd/MM/aaaa): '), '%d/%m/%Y')
    value_per_hour = float(input('Value Per Hour: '))
    duration = int(input('Hours: '))

    worker.add_contract(HourContract(date, value_per_hour, duration))

print()
date_income_text = input('Enter month and year to calculate income (MM/aaaa): ')
date_income = datetime.strptime(date_income_text, '%m/%Y')
total = worker.income(date_income.year, date_income.month)

print()
print(f'Name: {worker.name}')
print(f'Department: {worker.department}')
print(f'Income for {date_income_text}: R$ {total:.2f}')

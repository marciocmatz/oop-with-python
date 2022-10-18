from entities import Employee

name = input('Name: ')
gross_salary = float(input('Gross Salary: '))
tax = float(input('Tax: '))

employee = Employee(name, gross_salary, tax)

print()
print(f'Employee: {employee.name}, R$ {employee.net_salary():.2f}')

print()

percentage = float(input('Which percentage to increase salary?: '))
employee.increase_salary(percentage)

print()
print(f'Updated data: {employee.name}, R$ {employee.net_salary():.2f}')

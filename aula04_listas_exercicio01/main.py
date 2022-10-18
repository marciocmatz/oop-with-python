from entities import Employee
import sys

n = int(input('How many employees will be registered? '))
employees = []
ids = []

for i in range(1, (n + 1)):

    print()
    print('Employee #' + str(i))

    id_funcionario = int(input('ID: '))
    if id_funcionario in ids:
        print('--> ID JÁ EXISTE <--')
        sys.exit()

    name = input('Name: ')


    salary = float(input('Salary: '))

    ids.append(id_funcionario)
    employees.append(Employee(id_funcionario, name, salary))


print()
id_update = int(input('Enter the employee id that will have salary increase: '))


if id_update in ids:
    percentage = float(input('Enter percentage: '))

    for emp in employees:
        if id_update == emp.id_funcionario:
            emp.increase_salary(percentage)
else:
    print()
    print('--> ID INEXISTENTE <--')

print()
for emp in employees:
    print(emp)

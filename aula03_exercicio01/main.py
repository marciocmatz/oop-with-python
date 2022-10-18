from entities import Account

acc_number = int(input('Enter account number: '))
acc_holder = input('Enter account holder: ')
controle = input('Is there an initial deposit (y/n)? ')


if controle == 'y':
    initial_deposit = float(input('Enter initial deposit: '))
    acc = Account(acc_number, acc_holder, initial_deposit)
else:
    acc = Account(acc_number, acc_holder, 0)

print()
print('Account Data:')
print(f'Account: {acc.acc_number} / Holder: {acc.acc_holder} / Balance: {acc.balance:.2f}')

print()
deposit_value = float(input('Enter a deposit value: '))
acc.deposit(deposit_value)
print('UPDATED Account Data:')
print(f'Account: {acc.acc_number} / Holder: {acc.acc_holder} / Balance: {acc.balance:.2f}')

print()
withdraw_value = float(input('Enter a withdraw value: '))
acc.withdraw(withdraw_value)
print('UPDATED Account Data:')
print(f'Account: {acc.acc_number} / Holder: {acc.acc_holder} / Balance: {acc.balance:.2f}')

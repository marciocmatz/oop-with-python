from entities import CurencyConverter

dollar_price = float(input('What is the dollar price? '))
dollars = float(input('How many dollars will be bought? '))

totalValue = CurencyConverter().currency_converter(dollars, dollar_price)

print(f'Amount to be paid in reais = R$ {totalValue:.2f}')

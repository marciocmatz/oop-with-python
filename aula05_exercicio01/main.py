from entities import Client, Order, Product, OrderItem
from datetime import datetime

print('Enter client data:')
name = input('Name: ')
email = input('Email: ')
birth_date = datetime.strptime(input('Birth Date (dd/mm/aaa) '), '%d/%m/%Y')

client = Client(name, email, birth_date)
order = Order()

print()
print('Enter order data:')
n = int(input('How many items to this order: '))

for i in range(1, n + 1):
    print()
    print(f'Enter #{i} item data:')
    product_name = input('Product Name: ')
    product_price = float(input('Product Price: '))
    product_quantity = int(input('Product Quantity: '))

    product = Product(product_name, product_price)
    order_item = OrderItem(product_quantity, product_price, product)
    order.add_item(order_item)

print()
print('->> ORDER SUMARY <--')
print()
print(f'Order Moment: {"{}/{}/{}".format(order.moment.day, order.moment.month, order.moment.year)}')
print(f'Client: {client}')
print('Order items:')

for order in order.orders:
    print(order)

# total = order.total()
# print(f'TOTAL PRICE: R$ {total:.2f}')

print(order)

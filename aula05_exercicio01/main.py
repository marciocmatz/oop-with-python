from datetime import datetime
from entities import Client, Product, OrderItem, Order

print('Enter client data:')
client_name = input('Name: ')
client_email = input('Email: ')
client_birth_date = datetime.strptime(input('Birth Date: '), '%d/%m/%Y')

client = Client(client_name, client_email, client_birth_date)
order = Order()

print()
print('Enter Order Data:')
n = int(input('How many items to this order? '))

for i in range(1, n + 1):
    print()
    print(f'Enter #{i} item data:')
    product_name = input('Product Name: ')
    product_price = float(input('Product Price: '))
    product_quantity = int(input('Product Quantity: '))

    product = Product(product_name, product_price)
    order_item = OrderItem(product, product_quantity, product_price)

    order.add_item(order_item)

print()
print('ORDER SUMMARY:')
print(f'Order Moment: {order.get_moment()}')
print(client)
print('Order Items:')

for item in order.get_items():
    print(f'{item.get_product().get_name()}, R${item.get_price():.2f}, Quantity: {item.get_quantity()}, Subtotal: R${item.sub_total():.2f}')

total = order.total()
print(f'TOTAL PRICE: R${total:.2f}')

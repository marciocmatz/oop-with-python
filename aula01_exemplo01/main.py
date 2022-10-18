from entities import Product

print('Enter product data:')
name = input('Name: ')
price = float(input('Price: '))
quantity = int(input('Quantity: '))

print()
product = Product(name, price, quantity)

print(product)
print()

new_quantity = int(input('Enter the number of products to be added in stock: '))
product.add_products(new_quantity)

print()
print(product)
print()

remove_quantity = int(input('Enter the number of products to be removed from stock: '))
product.remove_products(remove_quantity)

print()
print(product)

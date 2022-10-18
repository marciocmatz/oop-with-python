from entities import Product

product = Product('Televisão', 200.00)

print(product.name)
print(product.price)

print()
# Aqui está sendo feito um set. O Python tem suas particularidades...
product.name = 'Televisão 2'
product.price = 300

print(product.name)
print(product.price)


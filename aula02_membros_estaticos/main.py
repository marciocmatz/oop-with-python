from util import Calculator

radius = float(input('Enter radius: '))

c = Calculator().circumference(radius)
v = Calculator().volume(radius)

print(f'Circumference: {c:.2f}')
print(f'Volume: {v:.2f}')

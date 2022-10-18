from entities import Triangle

x = Triangle()
y = Triangle()

print('Insira os dados do triangulo X:')
x.a = float(input())
x.b = float(input())
x.c = float(input())

print('Insira os dados do triangulo Y:')
y.a = float(input())
y.b = float(input())
y.c = float(input())

if (x.area() > y.area()):
    print('Triangulo X é maior que triângulo Y.')
elif (x.area() == y.area()):
    print('Triangulo X é igual ao triângulo Y.')
else:
    print('Triangulo X é menor que triângulo Y.')

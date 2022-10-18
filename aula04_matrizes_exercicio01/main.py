m = int(input('Digite o número de linhas da matriz: '))
n = int(input('Digite o número de colunas da matriz: '))

matriz = [[0 for _ in range(n)] for _ in range(m)]

print()
print('Digite os números da matriz:')
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input())

print()
num = int(input('Digite o número que deseja pesquisar: '))
print()

for i in range(m):
    for j in range(n):

        if (matriz[i][j] == num):
            print(f'POSITION: {i + 1}, {j + 1}')

        if (matriz[i][j] == num) and (i > 0):
            print(f'UP: {matriz[i - 1][j]}')

        if (matriz[i][j] == num) and (i < m - 1):
            print(f'DOWN: {matriz[i + 1][j]}')

        if (matriz[i][j] == num) and (j > 0):
            print(f'LEFT: {matriz[i][j - 1]}')

        if (matriz[i][j] == num) and (j < n - 1):
            print(f'RIGHT: {matriz[i][j + 1]}')

    print()

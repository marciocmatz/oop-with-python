matriz = [[0 for _ in range(5)] for _ in range(3)]

diagonal_principal = []
diagonal_secundaria = []

print()
print('Digite os números da matriz:')
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input())

# Replicando duas colunas para cálculo do determinante.
matriz[0][3] = matriz[0][0]
matriz[0][4] = matriz[0][1]

matriz[1][3] = matriz[1][0]
matriz[1][4] = matriz[1][1]

matriz[2][3] = matriz[2][0]
matriz[2][4] = matriz[2][1]

# Diagonais
soma_principal = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][3] + matriz[0][2] * matriz[1][3] * matriz[2][4]

soma_secundaria = matriz[0][2] * matriz[1][1] * matriz[2][0] + matriz[0][3] * matriz[1][2] * matriz[2][1] + matriz[0][4] * matriz[1][3] * matriz[2][2] 

det = soma_principal - soma_secundaria
print(f'DET = {det}')

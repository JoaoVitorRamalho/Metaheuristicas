matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        numero = int(input(f'Digite o valor da posição[{i}][{j}]: '))
        linha.append(numero)
    matriz.append(linha)

def identidade(matriz):
    for i in range(5):
        for j in range(5):
            if i == j:
                if matriz[i][j] != 1:
                    return False
            else:
                if matriz[i][j] != 0:
                    return False
            return True

ident = identidade(matriz)
if ident:
    print('É identidade')
else:
    print('Não é identidade')
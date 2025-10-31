matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        numero = int(input(f'Digite o valor da posição[{i}][{j}]: '))
        linha.append(numero)
    matriz.append(linha)

for linha in matriz:
    print(linha)
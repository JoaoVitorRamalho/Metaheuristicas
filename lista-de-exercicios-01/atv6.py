pessoas = []
for c in range(5):
    nome = input(f'Digite o nome da pessoa {c}: ')
    idade = int(input(f'Digite a idade da pessoa {c}: '))
    tupla = (nome,idade)
    pessoas.append(tupla)

for c in pessoas:
    if c[1] >= 18:
        print(f'Olá {c[0]} você tem {c[1]} anos')
classe = []
aluno = {}
for c in range(10):
    aluno['nome'] = input(f'Digite o nome do aluno {c}: ')
    aluno['nota'] = float(input(f'Digite a nota do aluno {c}: '))
    classe.append(aluno.copy())

print(classe)
for a in classe:
    if a['nota'] >= 6.0:
        print(f'A nota de {a["nome"]} foi {a["nota"]}') 
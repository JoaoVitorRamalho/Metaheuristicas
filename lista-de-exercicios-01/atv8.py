turma = []
aluno = {}
maior = media = 0
while True:
    aluno['nome'] = input('Digite o nome do aluno (sair para encerrar): ')
    if aluno['nome'] in 'sair':
        break
    else:
        aluno['nota'] = float(input('Digite a nota do aluno: '))
        media += aluno['nota']
        if aluno['nota'] > maior:
            maior = aluno['nota']
        turma.append(aluno.copy())

media /= len(turma)
print(f'A média da turma foi {media:.2f}')
print('Alunos que ficaram com a nota acima da média: ',end=' ')
for c in turma:
    if c['nota'] > media:
        print(f'{c['nome']}',end=' ')
print('Fim')
print('A maior nota da turma foi de: ',end=' ')
for c in turma:
    if c['nota'] == maior:
        print(c['nome'])
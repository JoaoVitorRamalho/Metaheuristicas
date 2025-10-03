aluno = {
    'nome': 'João',
    'idade': 21,
    'curso': 'BSI'
}

print(aluno['nome'])

print(aluno)

aluno['idade'] += 1
print(aluno)

aluno['matricula'] = '20251010'

print(aluno)

del aluno['curso']
print(aluno)

mat = aluno.pop('matricula')
print(mat)
print(aluno)

if 'matricula' in aluno:
    print('SIM')
else:
    print('NÃO')

print(aluno.keys())

alunos = [
    {'nome': 'Joao', 'matricula': '20251010'},
    {'nome': 'Maria', 'matricula': '20251212'}
]

alunos.append({'nome':'Vitor', 'matricula': '20251919', 'curso':'BSI'})

print(alunos)

ponto = {'x':10,'y':20}

print(ponto.values())

print(ponto.items())
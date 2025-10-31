print('''Menu de Atividades
1 - Atividade 1
2 - Atividade 2
3 - Atividade 3
4 - Atividade 4
5 - Atividade 5
6 - Atividade 6
7 - Atividade 7
8 - Atividade 8
9 - Atividade 9
10 - Atividade 10
11 - Atividade 11
12 - Atividade 12
13 - Atividade 13
14 - Atividade 14''')
op = int(input('Escolha uma opção: '))
match op:
    case 1:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        cidade = input('Digite sua cidade: ')
        print(f'Olá {nome}! Você tem {idade} anos e mora em {cidade}')
    
    case 2:
       a = 1 
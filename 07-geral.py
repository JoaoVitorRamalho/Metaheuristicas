# nome = input('Digite seu nome: ')
# print(nome)

# x = int(input('Informe um número inteiro: '))
# y = int(input('Informe um número inteiro: '))
# z = x+y
# print(z)

# a = float(input('Agora informe um número real: '))
# a /= 2
# print(f'A metade é {a}')

# idade = int(input('Informe sua idade: '))
# if idade < 12:
#     print('Criança')
# elif idade <18:
#     print('Adolescente')
# else:
#     print('Adulto')

# match idade:
#     case 1:
#         print('Bebê')
#     case 7:
#         print('Criança')
#     case 18:
#         print('Adulto')
#     case 'adulto':
#         print('oi')
#     case _:
#         print('Desconhecido')

# resp = input('Digite sim ou nao ').lower()
# match resp:
#     case 'sim':
#         print('SIM')
#     case 'nao':
#         print('NÃO')
# i = 0
# while i <10:
#     print('Joao')
#     i +=1

# numero = int(input('Digite um número: '))
# fat = fat2 = 1
# i = 1
# while i <= numero:
#     fat *=i
#     i +=1
# print(fat)
# for c in range(1,numero+1):
#     fat2 *=c
# print(fat2)
nomes = ['João', 'Maria', 'Ana', 'Bruno','Pedro']
for a in nomes:
    print(a)
nomes.sort()
print(nomes)
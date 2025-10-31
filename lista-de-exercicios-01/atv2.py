ingresso = 50
idade = int(input('Digite sua idade: '))
if idade < 12 or idade > 60:
    print(f'Você tem um desconto no valor do ingresso, ele custa {ingresso} reais, porém o valor que você irá pagar é {ingresso/2}')
else:
    print(f'Você não teve desconto no valor do ingresso, o valor a ser pago é {ingresso} reais')
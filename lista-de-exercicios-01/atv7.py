frutas = set()
repetidas = 0
while True:
    fruta = input('Digite uma fruta (sair para encerrar): ').strip().lower()
    if fruta in 'sair':
        break
    elif fruta in frutas:
        repetidas += 1
    else:
        frutas.add(fruta)

print(f'Frutas cadastradas: {frutas}\nNão foram cadastradas {repetidas} frutas')
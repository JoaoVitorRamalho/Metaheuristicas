paisA = int(input('Digite a quantidade de habitantes do pais A: '))
txcA = float(input('Digite a taxa de crescimento do pais A (em %): '))
paisB = int(input('Digite a quantidade de habitantes do pais B: '))
txcB = float(input('Digite a taxa de crescimento do pais B (em %): '))
txcA = txcA/100
txcB = txcB/100
anos = 0
while paisB > paisA:
    paisA += paisA*txcA
    paisB += paisB*txcB
    anos += 1

print(f'No ano de {2025+anos} o pais A tem {paisA} habitantes e o pais B tem {paisB} habitantes, levou {anos} para que o A ultrapassasse o B')
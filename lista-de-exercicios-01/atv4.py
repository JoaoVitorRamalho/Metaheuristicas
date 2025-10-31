paisA = 80000
txcA = 0.03
paisB = 200000
txcB = 0.015
anos = 0
while paisB > paisA:
    paisA += paisA*txcA
    paisB += paisB*txcB
    anos += 1

print(f'No ano de {2025+anos} o pais A tem {paisA} habitantes e o pais B tem {paisB} habitantes, levou {anos} para que o A ultrapassasse o B')
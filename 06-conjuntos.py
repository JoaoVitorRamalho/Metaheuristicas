numeros = {1,2,3,4,4,5}
print(numeros)
numeros = {6,1,2,3,4,4,5}
print(numeros)
numeros.add(7)
print(numeros)
numeros.remove(3) #Remove do conjunto / da erro se o número não existir no conjunto
print(numeros)
numeros.discard(3) #Remove se existir

numeros.clear() #Limpa o conunto
print(numeros)

pares = {2,4,6,8}
impares = {1,3,5,7}

u = pares | impares #união
print(u)

p2 = {4,5,6}
i = pares & p2 #interseção
print(i)

p3 = {2,6}
d = pares - p3 #diferença
print(d)

p4 = {4,6,10}
print(pares ^ p4)
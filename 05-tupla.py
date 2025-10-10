coordenada = (10,20)
print(coordenada)

#Tupla é imutável
#coordenada[0] = 50
#isso não funciona

print(coordenada[1])

cores = ('vermelho','verde','azul','branco','azul')
print(len(cores))

print(cores.count('azul'))

print(cores.index('azul'))

print(cores[1:3]) #do 1 até o 2
print(cores[:2]) #do primeiro até o anterior do 2
print(cores[-2:]) #os dois ultimos

ponto = (99,200)
#desenpacotamento
x, y = ponto

print(x)
print(y)

t = (10, 20, (30,40))

print(t[2])
print(t[2][1])

t1 = (1,2,3)
t2 = (4,5)
r = t1 + t2
print(r)

if 'verde' in cores:
    print('Sim')
else:
    print('Não')


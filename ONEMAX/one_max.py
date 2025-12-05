import random

def gera_solucao(n):
    s = []
    i = 0
    while i < n:
        s.append(random.randint(0,1))
        i += 1
    return s

def avalia_solucao(n):
    return sum(n)

def heuristica_aleatoria(n,interacoes):
    melhor_solucao = None
    melhor_avaliacao = -1

    i = 0
    while i < interacoes:
        solucao = gera_solucao(n)
        avaliacao = avalia_solucao(solucao)
        if avaliacao > melhor_avaliacao:
            melhor_solucao = solucao
            melhor_avaliacao = avaliacao
        i += 1

    return melhor_solucao, melhor_avaliacao

# a = gera_solucao(5)
# print(a)
# print(avalia_solucao(a))

s, a = heuristica_aleatoria(50,1000000.)

print(s)
print(a)
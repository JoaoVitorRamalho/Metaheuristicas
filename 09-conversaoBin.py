import random
import math
def bin2float(bits, a,b):
    g = 0
    n = len(bits)
    for c in range(n):
        g +=bits[c] * (2**(n - c - 1))

    return a + (g/(2**n-1)) * (b-a)

# b = [1,0,1,1,0]
# print (bin2float(b,0,10))

def f (x,y):
    z = 5 + math.sin(x) * math.sin(y) + 0.5 * math.sin(2*x) * math.sin(2*y) - 0.1 * (x**2 + y**2)
    return z

def gera_solucao(n):
    s = []
    for _ in range(n):
        s.append(random.randint(0,1))
    return s

def avalia_solucao(sol):
    min_x, max_x = -8,8
    min_y, max_y = -8,8
    n = len(sol)
    m = n//2
    sol_x = sol[:m]
    sol_y = sol[m:]
    x = bin2float(sol_x, min_x, max_x)
    y = bin2float(sol_y, min_y, max_y)
    return f(x,y)

# s = gera_solucao(30)
# print(s)
# z = avalia_solucao(s)
# print(z)

def hill_clibing (bits, max_it):
    sol_atual = gera_solucao(bits)
    fitness_atual = avalia_solucao(sol_atual)

    for _ in range(max_it):
        sol_vizinha = sol_atual.copy()
        r = random.randint(0, bits - 1)
        sol_vizinha[r] = 1 - sol_vizinha[r]
        fitness_vizinha = avalia_solucao(sol_vizinha)

        if fitness_vizinha > fitness_atual:
            sol_atual = sol_vizinha
            fitness_atual = fitness_vizinha

    return sol_atual, fitness_atual

sa, fa = hill_clibing(30,1000)
print(sa)
print(fa)
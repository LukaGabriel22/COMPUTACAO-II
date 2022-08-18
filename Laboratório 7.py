import numpy as np

#QUESTÃO 1

def gera_matriz(a, b, n, m):
    """Função recebe 4 elementos (a,b,n,m) e retorna um array numpy
    de formato MxM"""
    x = np.linspace(a,b,n)
    if m**2 == n:
        x.shape = (m,m)
        return x
    else:
        return('Não é possível construir')

# AS QUESTÕES 2 e 3 FORAM CORRIGIDAS EM AULA E PORTANTO, NÃO PRECISARAM SER FEITAS.

#QUESTÃO 4
    
def polinomio(x, coeficiente):
    """Função que calcula polinômios utilizando arrays e/ou funções de arrays
    int, float - > int, float"""
    X = np.ones_like(coeficiente)
    X[1:] = x
    y = np.cumprod(X)
    return coeficiente @ y



#QUESTÃO 5

import numpy as np
from random import uniform

class Variavel:
    
    """Gera uma matriz de desenhos de uma variável aleatória discreta com um‎
      vetor especificado de probabilidades.‎"""
    
    def __init__(self, q):
        self.q = q
        self.Q = np.cumsum(q)
        
    def draw(self, k = 1):
        return self.Q.searchsorted(uniform(0, 1, size = k))

def sample(q):
    a = 0.0
    U = uniform(0, 1)
    for i in range(len(q)):
        if a < U <= a + q[i]:
            return i, U
        a = a + q[i]

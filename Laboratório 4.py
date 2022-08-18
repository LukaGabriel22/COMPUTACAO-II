# QUESTÃO 1.

def piano(notas):
    
    """Essa função recebe uma string com os valores de uma nota musical e sua posição no piano, e retorna a
    frequência dessas notas nas diferentes partes de um piano.
    str - > list of floats"""
    
    reference = {'C': 262, 'D': 294, 'E': 330, 'F': 349, 'G': 392, 'A': 440, 'B': 494}
  
    # notando que 'notas' estão em posição par e 'posições' em posição ímpar
    notas_list = [notas[i] for i in range(0, len(notas), 2)]
    positions_list = [int(notas[i]) for i in range(1, len(notas), 2)]
    return [reference[key] * (2 ** (i - 3)) for i, key in zip(positions_list, notas_list)]


# QUESTÃO 2.

def elementos_distintos(elementos):
    """Função que recebe uma variável e retorna o número
    de elementos distintos (únicos) da variável recebida
    list -> int"""
    return len(set(elementos))

def testa_elementos_distintos():#Testes da função elementos_distintos
>>> elementos_distintos([1,2,3,1,2,3,4,5])
5
>>> elementos_distintos([1,1,2,2,3,3,4,4,5,5,6,6,7,8,9])
9

# QUESTÃO 5.
def resistor(cor1,cor2,cor3):
    """Recebe 3 strings que representam cores do código de um resistor, retorna 
    o valor da resistência baseado nos códigos de cores.
    str, str, str -> int"""
    
    faixas = {'preto': 0,'marrom': 1,'vermelho': 2,'laranja': 3,'amarelo': 4}
    for i in (cor1,cor2,cor3):
        if i not in faixas:
            faixas[i] = 0
            return("Código não encontrado",faixas[i])
        else:
            faixas[i] += 1
    return (faixas[cor1] * 10) + faixas[cor2] * (10 ** faixas[cor3])

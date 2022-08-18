from time import sleep

# QUESTÃO 1

def media_de_gols(jogador):
    """Dada uma matriz de jogadores adiciona a média de gols deles na lista dada.
    parâmetro -> jogador
    output -> jogador(agora com mais um elemento, sendo esse a média.)"""
    for i in range(len(jogador)):
        Numero_rodada = 3 + ValoresRodada.index(jogador[i][1])
            media_gols = jogador[i][2] / Numero_rodada
            jogador[i].append(mGols)
    return jogador


def artilheiros():
    """Lê e armazena em uma matriz diversas informações nesta ordem:
    Nome do jogador, Rodada, Numero de gols
    parâmetro -> none
    output-> list"""
    jogadores = []
    global ValoresRodada
    ValoresRodada = ["classificatoria", "oitavas", "quartas", "semi", "final"]
    while True:
        NomeDoJogador = input('Digite o nome do jogador (Fim para sair): ').capitalize()
        if NomeDoJogador == 'Fim':
            return media_de_gols(jogadores)
        while True:
            print("Digite em qual rodada ele parou")
            rodada = input('(Valores aceitos: classificatoria, oitavas, quartas, semi e final): ').lower()
            if rodada in ValoresRodada:
                break
            Numero_de_gols = int(input('Digite o número de gols: '))
            print(f'Jogador computado.')
            jogadores.append([NomeDoJogador, rodada, Numero_de_gols])
            sleep(2)


def main():
    melhores = artilheiros()
    MediaOuro = 0
    for i in range(len(melhores)):
        if melhores[i][3] > MediaOuro:
            NomeOuro = melhores[i][0]
            MediaOuro = melhores[i][3]
        print(f'O melhor jogador foi o {NomeOuro}, com uma média de gols de {MediaOuro :.2f}')
main()

from random import randint, sample

# QUESTÃO 2

def Sem_repeticao(valores):
    """Sorteará uma quantidade dada de números, tendo inicio e fim. Que não possua repetições.
    input -> inicio (valor inicial do intervalo de sorteio)
    fim (valor final do intervalo de sorteio)
    quantidade (quantidade de números sorteados)
    output -> lista (uma lista com números não repetidos sorteados)"""
    while True:
        num = randint(1, 60)
        if num not in valores:
            valores.append(num)
            return valores


def Fazer_cartela(numcartelas):
    """Definirá quais valores estão em cada cartela, e as armazenará em uma matriz.
    input-> nCartelas (Quantidade de cartelas)
    output -> matrizCartelas (Retorna a matriz com todos os valores de cada cartela)"""
    matrizCartelas = []
    for i in range(0, numcartelas):
        valoresCartela = sample(range(1, 61), 6)
        matrizCartelas.append(sorted(valoresCartela))
        return matrizCartelas


def EscolheCartela(numcartelas):
    """Faz o sorteio dos números e os compara. Se a interseção dos valores da cartela com o conjunto dos valores sorteados
    for igual aos próprios valores da cartela. Logo a cartela será premiada.
    input -> nCartelas (matriz com as cartelas)
    output -> A cartela sorteada"""
    conjuntoValores = []
    while True:
        conjuntoValores = Sem_repeticao(conjuntoValores)
            for i in numcartelas:
                if set(i) == set(i).intersection(conjuntoValores):
                    print(f'Os números sorteados, na ordem, foram: {conjuntoValores}')
                    return i


def main():
    numCartelas = int(input('Digite o número de cartelas participantes: '))
    matrizCartelas = FazCartela(numCartelas)
    cartelaSorteada = EscolheCartela(matrizCartelas)
    linhaSorteada = matrizCartelas.index(cartelaSorteada) + 1
    print(f"E a cartela vencedora foi a com valores: {cartelaSorteada}\n"
            f"Sendo a cartela de número: {linhaSorteada}")
main()

import random
import os


# QUESTÃO 3

def iniciar_jogo():
    """Função usada para iniciar o jogo; None -> None"""
    global memoria, descoberto
    valores = random.sample([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8], 16)
    memoria = [valores[0:4], valores[4:8], valores[8:12], valores[12:16]]
    descoberto = [[False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False],
                  [False, False, False, False]]
    return

def exibir_jogo():
    """Função usada para exibir o jogo; None -> None"""
    for i in range(0, 4):
        for j in range(0, 4):
            if descoberto[i][j]:
                print(memoria[i][j], end=' ')
            else:
                print('*', end=' ')
        print()
        
    
def revelar_posicao(l1, c1):
    """Função feita para revelar posições; int,int -> bool"""
    if descoberto[l1][c1] == False:
        descoberto[l1][c1] = True
        return True
    return False


def checar_posicoes(l1, c1, l2, c2):
    """Função para chegar as posições; int,int,int - > bool"""
    if memoria[l1][c1] == memoria[l2][c2]:
        print('\nParabéns! Você acertou!')
        return True
    else:
        print('\nVocê errou... Tente de novo.')
        esconder_posicoes(l1, c1, l2, c2)
    return False
    
    
def esconder_posicoes(l1, c1, l2, c2):
    """Função para esconder as posições; int,int,int,int -> none"""
    descoberto[l1][c1] = False
    descoberto[l2][c2] = False
    return


def checar_vitoria():
    """Função para chegar vitoria; none -> none"""
    for i in range(0, 4):
        if False in descoberto[i]:
            return False
    return True

iniciar_jogo()
jogadas = 0

def main():
    """Programa Principal onde fica a interface para o usuario inputar;none -> none"""
    contador = 0
    while True:
        os.system('cls || clear')
        
        r = list(range(0, 4))
        exibir_jogo()
        while True:
            pos1 = list(input('\nEscolha a primeira posição [x,y]: '))
            l1 = int(pos1[1])
            c1 = int(pos1[3])
            print()
            if l1 not in r or c1 not in r:
                input('Posição inválida. Escolha a primeira posição[x,y]:')
            elif not revelar_posicao(l1, c1):
                input('Posição inválida. Escolha a primeira posição[x,y]:')
            else:
                break
            
        exibir_jogo()
        
        while True:
            pos2 = list(input('\nEscolha a segunda posição [x,y]: '))
            print()
            l2 = int(pos2[1])
            c2 = int(pos2[3])
            if l2 not in r or c2 not in r:
                input('Posição inválida ou já escolhida. Escolha a segunda posição[x,y]:')
            elif not revelar_posicao(l2, c2):
                input('Posição inválida ou já escolhida. Escolha a segunda posição[x,y]:')
            else:
                break
        contador +=1

        exibir_jogo()
        checar_posicoes(l1, c1, l2, c2)
        if checar_vitoria():
             print(str.format('Parabéns! Você descobriu todas às casas em {} jogadas',contador))
             break


if __name__ == '__main__':
                   main()

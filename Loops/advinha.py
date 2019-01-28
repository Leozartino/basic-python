'''
Galera, eu desafio voces a fazer um jogo parecido com esse,
mas em vez do programa escrever "o número é maior" ou "o número é menor,"
o programa tem que escrever "Tá esquentando" ou "Tá esfriando"!
Dica: Voce vai ter q comparar os 2 últimos palpites e ver qual deles está mais próximo do número correto.
Se ninguém conseguir, eu posto a resposta aqui.
Esse desafio é perfeitamente possível com os conhecimentos que voces já aprenderam até o momento no curso. Então, sem desculpas!﻿

'''
from random import choice

numC = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numC = choice(numC)
numP = 11 #Inicializando com um valor que force o bloco do while ser executado, segundo suas condições.
tentativasf =  0

while numP != numC: #Enquanto esta condição for verdadeira execute os blocos:
    print('=-'* 21)
    print('-------Bem-vindo ao jogo da advinhação! :)-------\n')
    numP = int(input('Tente advinhar um número entre 0 e 10:\n'))
    tentativasf = tentativasf + 1

    if numP >= 0 and numP <= 10: #Intervalo válido, condição de verificação (validação)
        if numP == numC:
            print('\nParabéns você acertou!!\n')
        else:
            print('\nVocê errou, tente novamente\n')
            if numP < numC:
                print('\nUm valor um pouquinho maior... ;)\n')
            else:
                print('\nUm valor pouquinho menor... (; \n')
            ''' Considerando que a condição numP == numC será tratada uma única vez e que por isso anularia esta condicional,
                de imediato se tem implicitamente numP > numC, por isso else é conveniente por não gerar uma exceção neste caso. '''
    else:
        print('\nEntrada inválida, tente novamente\n')
print('=-'* 10)
print(f'\nO jogador tentou {tentativasf} vezes até acertar\n')
print('=-'* 10)

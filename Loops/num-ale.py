from random import choice
numC = []

for x in range (0,11):
    numC.append(x)

numC = choice(numC)

numJ = 11
tentativa = 0

while numC != numJ:

    numJ = int(input('\nBem-vindo ao jogo da advinhação !!\nInforme um número de 0 a 10:\n'))
    tentativa = tentativa + 1

    if numJ >= 0 and numJ <=10:
        if numC == numJ:
            print(f'\nParabéns, você acertou na {tentativa} tentativa\n')
        else:
            print('Você errou, tente novamente :)\n')
            if numJ < numC:
                print('Um valor maior...')
            else:
                print('Um valor menor...')
    else:
        print('\nEntrada invlida, tente novamente um número válido\n')       
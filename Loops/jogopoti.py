from random import choice
nome = str(input('\nInforme seu nome:\n')).capitalize()
cont = 0

while True:

    comp = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10] #Pode usar o radiant(n,x)
    chose_comp = choice(comp) #Poderia atualizar a variavel "comp", em vez de criar uma nova.
    jogador = int(input(f'\nInforme um valor entre 1 e 10:\n'))

    if jogador >=  1 and jogador <= 10:

        cond = str(input('\nVocê quer Par ou Ímpar?\n')).strip().capitalize()
        sum = chose_comp + jogador

        print('=-' *30)
        if cond == 'Par':
            if sum % 2 == 0:
                print(f'O jogador {nome} venceu\nO computador escolheu {chose_comp} e o jogador {jogador}')
                cont += 1
            else:
                print(f'O computador  venceu\nO computador escolheu {chose_comp} e o jogador {jogador}')
                break
        elif cond == 'Impar':
            if sum % 2 != 0:
                print(f'O jogador {nome} venceu\nO computador escolheu {chose_comp} e o jogador {jogador}')
                cont += 1
            else:
                print(f'O computador venceu\nO computador escolheu {chose_comp} e o jogador {jogador}')
                break
        else:
            print('\nResposta inválida, tente novamente\n')
        print('=-' *30)

    else:
        print('\nInforme um valor entre 1 e 10.\n')

if cont > 1:
    print(f'O jogador {nome} venceu {cont} vezes consecutivas')
elif cont == 1:
    print(f'O jogador {nome} venceu {cont} vez')
else:
    print(f'O jogador {nome} não venceu nenhuma vez')

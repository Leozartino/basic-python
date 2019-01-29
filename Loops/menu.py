from time import sleep
n1 = float(input('\nInforme um núemro:\n'))
n2 = float(input('\nInforme outro número\n'))
op = 0

while op != 5:
    sleep(1)
    print('''Menu:
    [1]-Soma
    [2]-Multiplicação
    [3]-Maior
    [4]-Novos números
    [5]-Para sair presione (5) \n''')

    '''
    Quando se põem a op para ser lida ao final das estruturas de decisão,
    de imediato é retornado "entrada inválida", pois não é substituido logo em seguida e o valor de op é validado pelas estruturas de seleção, o que não occore
    quando o a opção é lida logo após a exibição do menu, pois neste caso será susbstituido o valor
    definido inicialmente no programa pela entrada do usuário.
    '''
    op = int(input('\nQual é a sua opção?\n'))

    if op == 1:
        sum = n1 + n2
        sleep(0.5)
        print(f'A soma entre os dois número informados é {sum}\n')
    elif op == 2:
        mult = n1 * n2
        sleep(0.5)
        print(f'A multiplicação entre os dois números é: {mult}\n')
    elif op == 3:
        if n1 > n2:
            sleep(0.5)
            print(f'O maior número é {n1}\n')
        elif n2 > n1:
            sleep(0.5)
            print(f'O maior número é {n2}\n')
        else:
            sleep(0.5)
            print(f'Os dois números são iguais {n1} e {n2}')
    elif op == 4:
        sleep(0.5)
        n1 = float(input('\nInforme um núemro:\n'))
        n2 = float(input('\nInforme outro número\n'))
    elif op == 5:
        sleep(1)
        print('\nFinalizando...\n')
    else:
        print ('\nEntrada inválida')

print('Encerrado')

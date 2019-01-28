a = 1
cont = conti = neut = 0
neutro = False

while a != 0:
    num = int(input('\nInforme um valor inteiro:\n'))

    if num % 2 == 0 and num!=0:
        cont = cont + 1
    elif num == 0:
        neutro = True
        neut = neut + 1
    else:
        conti = conti + 1

    a = int(input('\nPara sair digite 0.\nPara continuar digite qualquer valor inteiro:\n'))

if neutro == True:
    print(f'\nFoi digitado {neut} neutro ou zero\n')
    print(f'\nForam digitados {cont} números pares e {conti} números ímpares\n')
else:
    print(f'\nForam digitados {cont} números pares e {conti} números ímpares\n')

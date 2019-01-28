termo = int(input('\nInforme o primeiro termo da PA:\n'))
raz = int(input('\nInforme a razão da PA:\n'))

listaPA = [termo]
cont = 1
R = 'S'
total = 0
mais = 10


while R == 'S':
    total = total + mais

    while cont < total:
        termo = termo + raz
        listaPA.append(termo)
        cont = cont + 1

    print(f'\nPA gerada com {total} termos : \n {listaPA}')
    R = str(input('Quer continuar informando termos? [S/N] \n ')).upper()

    if R == 'S':
        mais = int(input('\nInforme mais termos:\n'))
    else:
        print(f'\nTotal de termos gerados: {total} e os termos gerados foram: \n {listaPA}\n')

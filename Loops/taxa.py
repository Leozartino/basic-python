while True:
    popA = int(input('\nInforme o número de habitantes de A:\n'))
    taxaA = float(input('Informe a taxa de crescimento de A em %:\n'))
    popB = int(input('Informe o número de habitantes de B:\n'))
    taxaB = float(input('Informe a taxa de crescimento de B em %:\n'))

    if (taxaA < taxaB) or (popA > popB):
        print('\nInsira uma entrada válida')
    else:
        taxaA =  (taxaA/100)
        taxaB =  (taxaB/100)
        anos = 0
        while popA < popB:
            popA = popA + (popA * taxaA)
            popB = popB + (popB * taxaB)
            anos += 1
        print(f'\nEm {anos} anos a Popução A ultrapassará a População B.\nCaso a taxa de crescimento de ambas seja constante')
        r = str(input('\nQuer continuar? [S/N]\n')).upper().strip()
        if r == 'N':
            break
        while r!= 'S':
            r = str(input('\nQuer continuar? [S/N]\n')).upper().strip()
            if r == 'N':
                break
        if r == 'N':
            break




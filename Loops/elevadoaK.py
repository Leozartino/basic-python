n = int(input('\nInforme o valor de n: '))
k = int(input('\nInforme o valor de k: '))


if k >= 0:
    cont = 0
    resul = 1
    while cont < k :
        cont += 1
        resul = resul * n
    print(resul)
else: 
    print('\nInforme um valor válido')
        

num = int(input('\nInforme um numero para verificação:'))
cont = 1
c = 0
numeros = []

while cont <= num:  
    if num % cont == 0:
        c += 1
        numeros.append(cont)
    cont += 1

if c > 2:
    print(f'\nO numero {num} não é primo\nPode ser divido por {numeros}')
elif c <= 2:
    print(f'\nO número {num} é primo e só pode ser divido por {numeros}')             
    


n = int(input('\nInforme um valor inteiro:'))
cont = 0
s = 0

while cont < n:
    cont += 1
    s = s + 1/cont
    
print(f'\nA soma total foi: {s:.2f}')
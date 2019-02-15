from random import randint
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'\nOs numeros gerados foram {num}')

maior =  menor = num[0]

for x in range(0, len(num)):
    
    if num[x] > maior:
        maior = num[x]
    elif num[x] < menor:
        menor = num[x]

print(f'O maior numero gerado foi {maior} e menor foi {menor}')
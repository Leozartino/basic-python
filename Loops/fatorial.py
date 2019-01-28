num = int(input('\nInforme um número inteiro:\n'))
control = num
fat = 1

while control > 0:
    fat = fat * control
    control -= 1
    
print(f'\nO fatorial de {num} é: {fat}\n')

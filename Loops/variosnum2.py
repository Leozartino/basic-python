num = int(input('\nInforme um valor inteiro:\n'))
sum = cont = 0

while num != 999:
    num = int(input('\nInforme um valor inteiro:\n'))
    if num == 999:
        break
    sum+=num
    cont+=1

print('-=' * 30)
print(f'Foram somados: {cont} valores\nA soma foi: {sum}')
print('-=' * 30)

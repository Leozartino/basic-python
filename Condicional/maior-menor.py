maior = 0
menor = 0
elementos= []

for x in range (0, 5):

    num = float(input('\nInforme um numero:'))
    elementos.append(num)

    if x == 0:
        maior = menor = elementos[0]
    else:
        if elementos[x] > maior:
            maior = elementos[x]
        if elementos[x] < menor:
            menor = elementos[x]

print(f'O maior valor informado foi {maior} e o menor valor é {menor}')

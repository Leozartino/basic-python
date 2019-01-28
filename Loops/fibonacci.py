termo = int(input('\nInforme um número inteiro para a sequência:\n'))

f = 0
f1 = 1 
cont = 1
f2 = 1
#lista =[f1]
print(f'{f1}', end="->")

while cont < termo:
    f2 = f + f1
    f = f1
    f1 = f2
    print(f'{f2}', end="->")
    #lista.append(f2)
    cont +=1

print('Fim', end="")
#print(f'A sequência gerada foi: {lista}')

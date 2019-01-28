sum = contP = 0
menor = contador_do_menor = 0

while True:

    nomeP = str(input('\nInforme o nome do produto:  ')).strip()
    precoP = float(input('Informe o preço do produto: '))
    sum += precoP
    contador_do_menor += 1

    if precoP > 1000:
        contP += 1
    if contador_do_menor == 1 or precoP < menor:
        menor = precoP
        nomeB = nomeP

    r = str(input('Quer continuar? [S/N]  ')).strip().upper()[0]
    if r != 'S' and r == 'N':
        break
        
print('-=' * 30)
print(f'O total gasto é de {sum:.2f}R$\n{contP} produtos custam mais de 1000\nO produto mais barato é: {nomeB} e custa {menor}R$')
print('-=' * 30)

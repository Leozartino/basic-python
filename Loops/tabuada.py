
while True:
    cont = 0
    num = int(input('\nQual tabuada deseja ver?\n'))
    if num < 0:
        break
    print(f'A tabuada de {num} é:\n')
    while cont <= 10:
        print(f'{num} * {cont} = {num * cont}')
        cont += 1

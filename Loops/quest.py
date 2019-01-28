nome = str(input('\nInsira um nome: '))
while (len(nome)) <= 3:
    nome = str(input('\nInsira um nome maior que 3 caracteres: '))

idade = int(input('\nInforme sua idade: '))
while idade < 0 or idade > 150:
    idade = int(input('\nInforme sua idade: '))

salario = float(input('\nInforme o salario: '))
while salario < 0:
    salario = float(input('\nInforme o salario: '))

s = str(input('\nInforme seu genero: [M/F]: ')).upper().strip()
while s != 'M' and s != 'F':
    s = str(input('\nInforme seu genero: [M/F]: ')).upper().strip()

estadoC = str(input('\nInforme seu estado civil: [S-solteiro, C-casado, V-viuvo ou D-divorciado] ')).strip().upper()
while estadoC != 'S' and estadoC != 'C' and estadoC != 'V' and estadoC != 'D':
    estadoC = str(input('\nInforme seu estado civil: [S-solteiro, C-casado, V-viuvo ou D-divorciado] ')).strip().upper()

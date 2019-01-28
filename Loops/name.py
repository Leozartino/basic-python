
sexo = str(input('\nInforme seu sexo:')).upper()[0]

while sexo != 'M' and sexo != 'F':
        print('Entrada invalida, tente novamente')
        sexo = str(input('\nInforme seu sexo:')).upper()[0]

if sexo == 'M':
    print('Masculino')

elif sexo == 'F':
    print('Feminino')

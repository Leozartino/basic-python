s = str(input('\n Informe seu sexo: [F/M]\n')).upper()

while s != 'M' and s != 'F':
    print('\nInforme um sexo válido, por favor\n')
    s = str(input('Informe seu sexo: [F/M]\n')).upper()

if s == 'F':
    print('Seu sexo é Feminino')
elif s == 'M':
    print('Seu sexo é Masculino')

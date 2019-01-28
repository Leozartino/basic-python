m = idadef = idadep = p = 0

while True:
    s = str(input('Informe seu gênero: [M/F] ')).upper().strip()[0]

    if s == 'M' or s == 'F':
        p += 1
        idade = int(input('Informe sua idade: '))
        if s == 'M':
            print('Seu genero é Masculino')
            m += 1
        elif s == 'F':
            print('Seu genero é Feminino')
            if idade < 20:
                idadef += 1
        if idade > 18:
            idadep+=1
            
        r = str(input('Quer continuar? [S/N]\n')).upper()[0]
        if r == 'N':
            break
    else:
        print('\nInforme uma entrada válida para genero\n')
    print('-' * 30)

print('-=' * 30)
print(f'{p} pessoas foram cadastradas.\n{idadep} pessoas tem mais de 18 anos.\n{m} homens foram cadastrados.\n{idadef} mulheres tem menos de 20 anos.')
print('-=' * 30)

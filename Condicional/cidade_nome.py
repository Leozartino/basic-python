nome = str(input('Informe o nome:\n')).upper()

t = nome.split('ARDO')
a = t.replace(t[0],'Leon')
print(a)
if 'EDU' in nome:
    novo_nome = nome.replace('EDU','Leon').capitalize()
    print('Bem-vindo:', novo_nome,'nome legal esse, hein? (:')
else:
    print('Bem-vindo: ', nome.capitalize(), '!')

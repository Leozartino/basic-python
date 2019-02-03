'''
 Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
 Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
'''
frase1 = str(input('\nDigite uma frase:\n')).strip().capitalize()
frase2 = str(input('\nDigite outra frase:\n')).strip().capitalize()


print(f'\nA primeira frase tem {len(frase1)} caracteres incluindo espaços\nSeu conteúdo é: {frase1} ')
print(f'\nA segunda frase tem {len(frase2)} caracteres incluindo espaços\nSeu conteúdo é: {frase2}')

if len(frase1) == len(frase2):
    print('\nAs strings tem o mesmo comprimento')
else:
    print('\nAs strings são diferentes tem tamanho')

frase1 = frase1.split()
frase2 = frase2.split()        
frase1 = ''.join(frase1)
frase2 = ''.join(frase2)

if frase1 == frase2:
    print('\nAs duas strings possuem o mesmo conteúdo')
else:
    print('\nAs duas Strings são diferentes em conteúdo')
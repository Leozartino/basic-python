contagem = ('zero','um','dois', 'três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')

while True:
   num = int(input('\nInforme um numero entre 0-20:\n'))
   if 0 <= num <= 20:
    print(f'\nVocê digitou o número {contagem[num]}')
    r = str(input('\nVocê quer continuar? [S/N]')).upper()
    if r == 'N':
        break
   else:
    print('\nFora do intervalo')

print('\nFinalizado')
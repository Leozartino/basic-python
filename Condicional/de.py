Reais = float(input('Digite o valor em reais:\n'))
Meses = int(input('\nQuantos mêses você pretende ficar na Alemanha?\n'))

Euro = (Reais / 4.44)
Valor_mes = (Euro / Meses)

if Valor_mes >= 720.00:
    print('\nVocê atende um dos requisitos do visto para procurar emprego\n')
    print('Você terá {:.3f}€ por {} meses'.format(Valor_mes, Meses))
else:
    print('Infelizmente você não atende o requisto de custo por mês para esse visto')
    print('O valor de {:.3f} para {} meses é inferior ao que foi descrito (720.00€)'.format(Valor_mes, Meses))

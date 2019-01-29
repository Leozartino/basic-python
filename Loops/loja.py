'''
Uma loja tem 15 clientes cadastrados e deseja enviar uma correspondência a cada 
um deles anunciado um bônus especial. Faça um programa que leia o nome do cliente e 
o valor de suas compras no ano passado. Calcule e mostre um bônus de 10% se o valor
das compras for menor que R$ 1.000,00 e de 15%, caso contrário

'''
cliente = 15
control = 0

while control < cliente:
    nome = str(input('Digite o nome do cliente:\n')).strip().title()
    compras = float(input('Digite o valor da compra do cliente no ano passado:\n'))

    if compras <= 1000:
        bonus = compras * (10/100)
    else:
        bonus = compras * (15/100)
    # Em vez de usar um print em cada estruura de seleção, usar após os blocos exibi da mesma forma sem gerar mais linhas como na solução anterior           
    print(f'\nVocê recebeu um bonus na próxima compra de R$ {bonus:.2f}\n')
    control += 1
        


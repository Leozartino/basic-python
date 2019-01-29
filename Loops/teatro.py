'''
Um companhia de teatro planeja dar uma série de espetáculos. A direção calcula que, a 
R$ 5,00 o ingresso, serão vendidos 120 ingressos, e as despesas montarão em R$ 200,00. A 
diminuição de R$ 0,50 no preço dos ingressos espera-se que haja um aumento de 26 ingressos 
vendidos. 
Fazer um algoritmo que escreva uma tabela de valores do lucro esperado em função do 
preço do ingresso, fazendo-se varias este preço de R$ 5,00 a R$ 1,00 de R$ 0,50 em R$ 0,50. 
Escreva, ainda, o lucro máximo esperado, o preço e o número de ingressos correspondentes.

'''

preco = 5 
ingresso = 120
maximo = 0

while preco >= 1:
    vendas = preco * ingresso
    lucro = vendas - 200

    if lucro > maximo:
        maximo = lucro
        precoideal = preco
        qntingresso = ingresso

    print(f'Vendendo o ingresso a R$ {preco}, espera-se vender {ingresso} ingressos com lucro R${lucro}\n')
    preco = preco - 0.5
    ingresso = ingresso + 26

print(f'O valor máximo de lucro é de {maximo}, vendendo a R${precoideal} com {qntingresso} de ingressos vendidos')
    
    
    
        

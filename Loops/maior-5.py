control = 5
'''
Neste código não foi necessário inicializar a variavel maiorAtual, pois na consulta/validação
a expressão a ser comparada inicialmente é: control == 5 e de imediato ela é verdadeira sem o
"acionamento" da segunda expressão que geraria um erro, pois não há valor algum a ser comparado 
com num: num > maiorAtual.

Mas se caso a primeira expressão a ser comparada fosse: num > maiorAtual, considerando o mesmo cenário
seria acusado um erro, apesar do operador or existir na expressão no momento da intrepretação é 
verificado o que aparece primeiro e como não há valor para a variavel, é gerado o erro.
'''

while control > 0:
    
    num = int(input('\nDigite um número: '))
    if control == 5 or num > maiorAtual:
        maiorAtual = num
    control -= 1

print(f"\nO maior número digitado é: {maiorAtual}")
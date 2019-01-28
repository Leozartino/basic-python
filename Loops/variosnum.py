r = sum = cont = 0

'''
Se a variavel "r" for lida após o teste lógico, os blocos seguidos serão executados (nesse caso, soma e contagem)
Como a condição de parada (flag) também é um valor inteiro que pode ser somado,
o flag será computado como uma entrada válida e se misturarar com os valores "limpos";
O laço não será interrompido de imediato e por isso há o problema.

A solução para este problema seria ler o valor de "r" ao final do laço, garantido que a soma e a contagem não ocorram
de imediato e logo depos fosse feito o teste lógico no while, ou interromper o laço usando a condição de parada com "break".
(ver solução também no arquivo variosnum2.py)
'''
while r != 999: # como o while possui um teste lógico no ínicio, por a leitura ao final do laço, força ele a não verificar o 999 como entrada.
        sum  = sum + r
        cont += 1
        r = int(input('\nInforme um valor inteiro:\n'))

print(f'Foram digitados {cont} numeros e a soma de todos eles foi {sum}')

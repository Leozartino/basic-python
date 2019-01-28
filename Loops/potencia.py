n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

pot = 1
i   = 1

while  i <= k: #A variavel k "dita" o numero de vezes a ser repetido a mult
    pot = pot * n # mult o valor de p por n
    i   = i + 1 # contador, este valor sera comparado com a variavel k, quando a condição for falsa, isto é, o valor de i ultrapassar o valor de k, o loop encerra.

print("A potencia eh", pot)  # print mais simples

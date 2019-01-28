from random import choice

num = []
cont = 0

for x in range (0, 11):
    num.append(x)

print('=-' * 30)
c = choice(num)
p = int(input("\nTente adivinhar o número gerado pelo computador: [0-10]\n"))

if p == c:
    print('\nParabéns você acertou\n')
else:
    while p != c:
        cont += 1
        print('Você errou, tente novamente')
        p = int(input("\nTente adivinhar o número gerado pelo computador: [0-10]\n"))

if cont >= 3:
    print(f'\nVocâ acertou, efim!\nO jogador tentou {cont} vezes até acertar')
elif cont <= 2:
    print(f'\n Você acertou\nO jogador tentou {cont} vezes até acertar')
print('=-' * 30)

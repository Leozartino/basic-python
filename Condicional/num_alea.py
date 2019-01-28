from random import choice

num = []

for x in range (0,6):
    num.append(x)

c = choice(num)
p = int(input("\nTente adivinhar o número gerado pelo computador: [0,1,2,3,4,5]\n"))

if c == p:
    print(f"Wow!, você acertou. O numero gerado foi: {c} e sua escolha: {p}")
elif p>= 0 and p <=5:
    if c!=p:
        print(f"Você errou, o numero gerado foi: {c}")
else:
    print("\nEntrada inválida\n")

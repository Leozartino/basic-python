cont = 0
sum = 0

while cont < 5:
    num = int(input("\nDigite um valor inteiro:"))
    sum = sum + num
    cont += 1
    
media = sum/cont
print(f'\nA soma foi {sum} e a média dos números informados foi {media:.2f}')

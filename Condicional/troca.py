x = float(input('Informe um valor numerico:\n'))
y = float(input('Informe outro valor:\n'))

print(f'valor de x: {x}, valor de y: {y}\n')

temp = x
x = y
y = temp

print(f'Os valores trocador são x = {x} e , y= {y}')

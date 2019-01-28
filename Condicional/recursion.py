
a = float(input('Informe um valor:'))
b = float(input('Informe outro valor:'))

def mult(x,y):

    if (x == 0 or y == 0):
        return 0

    elif (y == 1 ):
        return x

    else:
        if x%1==0:
            return (y + mult(x-1, y))

        elif y%1==0:
            return (x + mult(x, y-1))



resultado = mult (a,b)

print('O valor da multiplicação foi de: {:.2f}'.format(resultado))

a = int(input('\nInforme algo:'))
b = int(input('\nInforme algo:'))
lista = ['a','b','c' ,'d']

def cal (x,y):
    sal = 0

    for c in lista:
        if x >= 10:
            sal = sal +  (x + y)
        else:
            sal = sal + (x + y ) * 2

    return sal

print(cal(a,b))

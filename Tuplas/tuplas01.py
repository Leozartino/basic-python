#Tuplas são imutáveis 

material = ('Caneta', 'Lápis', 'Caderno')

m = 0
while m < len(material):
    print(material[m])
    m += 1

for cont in material:
    print(cont) 

for x in range (0, len(material)):
    print(material[x])

for pos, a in enumerate(material):
    print(a, pos)
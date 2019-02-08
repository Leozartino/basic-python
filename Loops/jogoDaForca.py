'''
Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado..
'''
from random import choice

palavras = ['Açaí', 'Cupuaçu', 'Manga', 'Goiaba', 'Jaca', '']
palavras = choice(palavras)
palavra = palavras.upper()
c = []
index = 0
while index < len(palavra):
    c.append(palavra[index])
    index += 1

traco = ['_ '] * len(palavra)
cond = condV = 0


print('--------*--------')
print('Jogo da forca\nTema: Frutas')
print('--------*--------')
print(traco)

while True:
    letra = str(input('\nInforme uma palavra: ')).strip().upper()[0]
    indice =  contE = contA = 0
    #Loop para varrer a string e fazer a comparação durante o processo.
    while indice < (len(palavra)): 
        if letra == palavra[indice]:
             traco[indice] = letra
             contA += 1
        else:
            contE += 1
        indice += 1

    print(traco)

    if traco == c:
        print('\nVoce ganhou!')
        break
    if contE == len(palavra):
        cond += 1
  
    if cond == 6:
        print('\nGame Over!')
        break


        
            






    





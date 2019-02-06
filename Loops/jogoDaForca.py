'''
Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado..
'''
from random import choice

palavras = ['Açaí', 'Cupuaçu', 'Manga', 'Goiaba']
palavras = choice(palavras)
palavra = palavras.upper()
traco = ['_ '] * len(palavra)

print(traco)
print('--------*--------')
print('Jogo da forca\nTema: Frutas')
print('--------*--------')

while True:
    letra = str(input('\nInforme uma palavra: ')).strip().upper()[0]
    indice = 0
    contA = contE = 0
    #Loop para varrer a string e fazer a comparação durante o processo.
    while indice <= (len(palavra)-1):
        if letra == palavra[indice]:
            traco[indice] = letra
            contA += 1
        indice += 1
    if contA == 0:
        contE += 1              
    print(traco)
    if contE == 6:
        break
        
            






    





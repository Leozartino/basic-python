'''
Desenvolva um jogo da forca. 
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado..
'''
from random import choice

palavras = ['Açaí', 'Cupuaçu', 'Manga', 'Goiaba']
palavras = choice(palavras)
palavra = palavras.upper()

print('--------*--------')
print('Jogo da forca\nTema: Frutas')
print('--------*--------')
advinha = str(input('Informe uma letra: ')).strip().capitalize()

if advinha[0] in palavra.upper():
    print(palavra.count(advinha))
    #Criar um loop para varrer a string e fazer a comparação durante o processo.
    print(palavra.find(advinha))



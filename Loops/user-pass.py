nome = str(input('\nInforme seu nome:  ')).strip().capitalize()
senha = str(input('Crie uma senha:  ')).strip().capitalize()

while senha == nome:
    nome = str(input('\nInforme seu nome:  ')).strip().capitalize()
    senha = str(input('Crie uma senha:  ')).strip().capitalize()

   

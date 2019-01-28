s = str(input('\nInsira uma string: \nCaso ela tenha o caractere "a", este sera susbstituido por "e": ')).strip().lower()

contador = s.count('a')

if contador > 0:
    s = s.replace('a','e')

print(s.capitalize())
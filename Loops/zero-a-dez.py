while True:
    nota = float(input('\nInsira uma nota entre 0 e 10:\n'))
    if nota < 0 or nota > 10:
        print('Nota entre 0 e 10.\nInsira um valor válido')
    else:
        break

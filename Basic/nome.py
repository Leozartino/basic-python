nome = str(input('\nInforme um nome: ')).strip().title().split()

ns = []
ns.append(nome[0])
ns.append(nome[(len(nome)-1)])
ns = ' '.join(ns)

''' Como a contagem de strings/vetor começa em [0] 
    e o metodo len retorna o tamnho inicializando em 1 (caso não seja vazia)
    é necessário subtrair -1 do retorno de len, já que os valores de posição e tamanho
    estão em desacordo, igualando asism, ao valor da posição da string/lista.                                                                        '''

print(f'\nO primeiro nome é {nome[0]} e o último nome é {nome[len(nome)-1]}')
print(f'\nBem-vindo {ns}')
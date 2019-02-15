brasileirao = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia','Fluminense','Corinthias','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')

print(f'\nOs 5 primeiros colados do brasileirão são {brasileirao[0:5]}')
print(f'\nOs últimos 4 colocados da tabela são {brasileirao[-4:]}')
print(f'\nEm ordem alfabética {sorted(brasileirao)}')

for inde in range (0, len(brasileirao)):
    if brasileirao[inde] == 'Chapecoense':
        print(f'\nO time Chapecoense está na posição {inde+1}ª')
"""
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa 
anual de crescimento de 3% \e que a população de B seja 200.000 habitantes com uma taxa de 
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento
"""
popA, popB, anos = 80000, 200000, 0
cresA, cresB = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano

while (popA < popB):
    anos += 1
    popA = popA + (popA * cresA)
    popB = popB + (popB * cresB)

print(f'Após {anos} anos o país A ultrapassou o país B em número de habitantes.')
print(f'País A: {popA:.2f}')
print(f'País B: {popB:.2f}')
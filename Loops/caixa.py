
pop_A = 800
pop_B = 2000

taxa_A = pop_A * 0.3
taxa_B = pop_B * (1.5/100)

cont = 1

while pop_A < pop_B:
    PopA = (pop_A + (taxa_A * cont))
    PopB = (pop_B + (taxa_B * cont))
    
print(PopA, pop_B)
with open ('rosalind_revc.txt') as file:
            dna = file.read()
mut_dna = dna[::-1]
mut_dna_low = mut_dna.lower()
dna_comp = mut_dna_low.replace('a', 'T').replace('c', 'G').replace('g', 'C').replace('t', 'A')
print(dna_comp)

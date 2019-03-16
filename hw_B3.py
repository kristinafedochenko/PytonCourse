with open ('C:/Users/Настюша/Downloads/rosalind_hamm.txt') as file:
        a = file.readline()
        b = file.readline()
Q = len(a)
count_dna = 0
for i in range(Q):
    if a[i] == b[i]:
        continue
    else:
        count_dna += 1
print(count_dna)


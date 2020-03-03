array = input().split(' ')
M = int(array[0])
P = int(array[1])
L = int(array[2])
E = int(array[3])
R = int(array[4])
S = int(array[5])
N = int(array[6])

for i in range(1, N + 1):
    mosquitos = M
    laidEggs = M * E
    larvae = L - (L - R)
    pupae = P - (P - S)

    L += E

print(M)

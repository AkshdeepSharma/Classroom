info = input().split(' ')

B = int(info[0])
Br = int(info[1])
Bs = int(info[2])
A = int(info[3])
As = int(info[4])

bobsaved = (Br - B) * Bs
alicesaved = 0

while alicesaved <= bobsaved:
    alicesaved += As
    A += 1

print(str(A))

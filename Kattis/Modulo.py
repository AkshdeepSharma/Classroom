
listToDivide = []
modulo = []

for i in range(10):
    a = int(input())
    listToDivide.append(a)

for j in range(10):
    c = listToDivide[j] % 42
    modulo.append(c)

setModulo = set(modulo)

print(len(setModulo))

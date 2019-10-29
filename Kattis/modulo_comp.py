numbers = []
modulos = []

for i in range(10):
    numbers.append(int(input()))


for j in numbers:
    if j % 42 not in modulos:
        modulos.append(j % 42)

print(len(modulos))
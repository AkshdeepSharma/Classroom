N = input()
t = input().split(' ')
cold = 0
for i in t:
    i = int(i)
    if i < 0:
        cold += 1

print(str(cold))

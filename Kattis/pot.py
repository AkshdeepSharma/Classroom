N = int(input())
value = 0
for i in range(N):
    num = input()
    power = int(num[-1])
    num = int(num[:-1])
    value += num ** power

print(value)

aandb = input().split(' ')
a = int(aandb[0][::-1])
b = int(aandb[1][::-1])

print(a if a > b else b)

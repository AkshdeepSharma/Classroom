num = int(input())
reverseBinary = ''
output = 0
while True:
    reverseBinary += str(num % 2)
    if num == 1:
        break
    num = num // 2

binary = reverseBinary[::-1]

for i in range(len(binary)):
    output += int(binary[i]) * 2 ** i

print(output)

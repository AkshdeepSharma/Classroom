def phoneList(n):
    phone_numbers = []
    for _ in range(n):
        phone_numbers.append(input())
    phone_numbers.sort()
    for i, val in enumerate(phone_numbers):
        for j in range(i + 1, len(phone_numbers)):
            if phone_numbers[j].startswith(val):
                return "NO"
            break
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    print(phoneList(n))
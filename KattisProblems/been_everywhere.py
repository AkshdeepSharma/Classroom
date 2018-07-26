T = int(input())
for i in range(T):
    n = int(input())
    cities = {}
    for j in range(n):
        city = input()
        if city not in cities:
            cities.update({city: 1})
    print(len(cities))

T = int(input())

for i in range(T):
    cities = []
    n = int(input())
    for j in range(n):
        city = input()
        cities.append(city)
    uniqueCities = set(cities)
    print(len(uniqueCities))

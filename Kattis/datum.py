day = {
    0: "Wednesday",
    1: "Thursday",
    2: "Friday",
    3: "Saturday",
    4: "Sunday",
    5: "Monday",
    6: "Tuesday",
}

month = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
}

D, M = map(int, input().split())

for i in range(M - 1):
    D += month[i]

print(day[D % 7])

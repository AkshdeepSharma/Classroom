N = int(input())
days = list(map(int, input().split(" ")))
max_temp, day_to_leave = max(days[0], days[2]), 1

for i in range(len(days) - 2):
    d1, d2 = days[i], days[i + 2]
    max_d = max(days[i], days[i + 2])
    if max_d < max_temp:
        max_temp = max_d
        day_to_leave = i + 1

print(str(day_to_leave) + " " + str(max_temp))

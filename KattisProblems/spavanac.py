clock = input().split(' ')
hours, minutes = int(clock[0]), int(clock[1])


if hours == 0 and minutes <= 44:
    hours = 23
    minutes = 60 - (45 - minutes)
elif minutes <= 44:
    hours -= 1
    minutes = 60 - (45 - minutes)
else:
    minutes -= 45

print(hours, minutes)

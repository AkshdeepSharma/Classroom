try:
    while True:
        date = input().split(' ')
        sunrise = date[3].split(':')
        sunset = date[4].split(':')
        hours = int(sunset[0]) - int(sunrise[0])
        minutes = int(sunset[1]) - int(sunrise[1])
        if minutes < 0:
            minutes = minutes + 60
            hours -= 1

        print(date[0], date[1], date[2], hours, "hours", minutes, "minutes")
except EOFError:
    pass

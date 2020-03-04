def isItFriday(curr_date, curr_day):
    days_of_week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    INDEX = days_of_week.index(curr_day)
    days_of_week[:] = days_of_week[INDEX:] + days_of_week[:INDEX]
    months = {
        "FEB": 31,
        "MAR": 60,
        "APR": 91,
        "MAY": 121,
        "JUN": 152,
        "JUL": 182,
        "AUG": 213,
        "SEP": 244,
        "OCT": 274,
        "NOV": 305,
        "DEC": 335,
    }
    day = int(curr_date[0])
    if curr_date[1] != "JAN":
        day += months[curr_date[1]]

    return_day = days_of_week[(day % 7) - 1]
    if (return_day == "FRI" or return_day == "SAT") and curr_date[1] not in ("JAN", "FEB"):
        return "not sure"
    if return_day == "FRI" or (return_day == "FRI" and curr_date == ["29", "FEB"]):
        return "TGIF"
    return ":("


def main():
    curr_date = input().split()
    curr_day = input()
    print(isItFriday(curr_date, curr_day))


if __name__ == "__main__":
    main()

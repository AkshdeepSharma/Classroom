def main():
    year_to_check = int(input())
    month, year = 4, 2018
    while year < year_to_check:
        year += 2
        month += 2
        if month > 12:
            month -= 12
            year += 1
    if year_to_check == year:
        print('yes')
    else:
        print('no')


if __name__ == "__main__":
    main()

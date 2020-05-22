def main():
    mini, maxi = 1, 10
    while True:
        num = int(input())
        if num == 0:
            break
        response = input()
        if response == 'right on':
            if mini > num or num > maxi:
                print('Stan is dishonest')
            else:
                print('Stan may be honest')
            mini, maxi = 1, 10
        elif response == 'too low' and num >= mini:
            mini = num + 1
        elif response == 'too high' and num <= maxi:
            maxi = num - 1


if __name__ == "__main__":
    main()

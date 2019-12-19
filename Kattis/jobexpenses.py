def main():
    N = input()
    income_expenses = list(map(int, input().split()))
    expenses = 0
    for expense in income_expenses:
        if expense < 0:
            expenses += expense * -1
    print(expenses)


if __name__ == '__main__':
    main()

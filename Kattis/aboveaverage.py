def studentsAboveAverage(students, grades, average):
    count = 0
    for grade in grades:
        if grade > average:
            count += 1
    return f"{count / students * 100: .3f}" + "%"


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        inp = list(map(int, input().split()))
        students, grades = inp[0], inp[1:]
        average = sum(grades) / students
        print(studentsAboveAverage(students, grades, average))


if __name__ == "__main__":
    main()

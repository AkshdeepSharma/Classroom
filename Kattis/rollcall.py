def getStudentsInOrder(students):
    students = sorted(students, key=lambda x: (x[1], x[0]))
    ans = []
    duplicate_names = {}
    for first_name, last_name in students:
        if first_name not in duplicate_names:
            duplicate_names[first_name] = 0
        duplicate_names[first_name] += 1
    for first_name, last_name in students:
        if duplicate_names[first_name] > 1:
            ans.append(f"{first_name} {last_name}")
        else:
            ans.append(first_name)
    return ans


def main():
    students = []
    try:
        while True:
            students.append(input().split())
    except EOFError:
        pass
    ans = getStudentsInOrder(students)
    for student in ans:
        print(student)


if __name__ == "__main__":
    main()

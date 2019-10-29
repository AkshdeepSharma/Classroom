def hayPoints(dictionary, job_description):
    salary = 0
    job_description = job_description.split()
    for word in job_description:
        if word in dictionary:
            salary += dictionary[word]
    return salary

if __name__ == "__main__":
    dic = {}
    mn = input().split()
    m, n = int(mn[0]), int(mn[1])
    for i in range(m):
        word = input().split()
        dic[word[0]] = int(word[1])
    for j in range(n):
        temp = job_description = ""
        while temp != ".":
            job_description += temp + " "
            temp = input()
        print(hayPoints(dic, job_description))

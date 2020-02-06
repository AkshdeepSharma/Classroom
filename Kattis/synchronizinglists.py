def synchronize(l1, l2):
    d = {}
    copy_l1 = sorted(l1[:])
    l2 = sorted(l2)
    for i in range(len(copy_l1)):
        d[copy_l1[i]] = l2[i]
    l2 = []
    for i in range(len(l1)):
        l2.append(d[l1[i]])
    return l2


def main():
    n = int(input())
    while n != 0:
        l1, l2 = [], []
        for _ in range(n):
            l1.append(int(input()))
        for _ in range(n):
            l2.append(int(input()))
        l2 = synchronize(l1, l2)
        for num in l2:
            print(num)
        print("")
        n = int(input())


if __name__ == "__main__":
    main()

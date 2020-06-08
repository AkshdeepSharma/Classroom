def main():
    n = int(input())
    while n != 0:
        ans = []
        orders = {}
        for _ in range(n):
            order = input().split()
            for i in range(1, len(order)):
                if order[i] not in orders:
                    orders[order[i]] = [order[0]]
                else:
                    orders[order[i]].append(order[0])
        for key, val in orders.items():
            ans.append([key] + sorted(val))
        ans = sorted(ans)
        for line in ans:
            print(" ".join(line))
        print("")
        n = int(input())


if __name__ == "__main__":
    main()

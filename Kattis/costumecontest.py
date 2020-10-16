def getBestCategory(categories):
    value_min = categories[min(categories.keys(), key=lambda k: categories[k])]
    ans = []
    for key, val in categories.items():
        if val == value_min:
            ans.append(key)
    return sorted(ans)


def main():
    N = int(input())
    categories = {}
    for _ in range(N):
        category = input()
        if category not in categories:
            categories[category] = 0
        categories[category] += 1
    ans = getBestCategory(categories)
    for category in ans:
        print(category)


if __name__ == "__main__":
    main()

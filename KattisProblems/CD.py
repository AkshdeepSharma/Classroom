def countCD(cd1, cd2):
    hashset = set()
    sell = 0
    for _ in range(cd1):
        catalog_num = input()
        hashset.add(catalog_num)
    for _ in range(cd2):
        catalog_num = input()
        if catalog_num in hashset:
            sell += 1
    return sell

if __name__ == "__main__":
    while True:
        cd1, cd2 = map(int, input().split())
        if cd1 == 0 and cd2 == 0:
            break
        print(countCD(cd1, cd2))
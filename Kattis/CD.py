import sys


def helper(f, cd1, cd2):
    hashset = set()
    for _ in range(cd1 + cd2):
        catalog_num = f.readline()
        hashset.add(catalog_num)
    return cd1 + cd2 - len(hashset)


def countCD(f):
    while True:
        cd1, cd2 = map(int, f.readline().split())
        if cd1 == 0 and cd2 == 0:
            break
        yield helper(f, cd1, cd2)


def main(f):
    for result in countCD(f):
        print(result)


if __name__ == "__main__":
    main(sys.stdin)

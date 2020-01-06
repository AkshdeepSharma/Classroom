from math import sqrt


def create_map(order):
    hashmap = {}
    for i in range(3):
        for j in range(3):
            hashmap[order[i][j]] = (i, j)
    return hashmap


def calculate_length(hashmap):
    length = 0
    for i in range(2, 10):
        curr = str(i)
        x2, y2 = hashmap[str(i)]
        x1, y1 = hashmap[str(i - 1)]
        length += sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return length


def main():
    order = []
    for _ in range(3):
        order.append(input().split())
    hashmap = create_map(order)
    print(round(calculate_length(hashmap), 10))


if __name__ == "__main__":
    main()

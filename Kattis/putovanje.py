def countFruitToEat(fruits, capacity):
    max_fruits = 0
    for i in range(len(fruits)):
        curr_capacity = curr_fruits = 0
        for j in range(i, len(fruits)):
            if curr_capacity + fruits[j] <= capacity:
                curr_capacity += fruits[j]
                curr_fruits += 1
        max_fruits = max(max_fruits, curr_fruits)
    return max_fruits


def main():
    num_fruit, capacity = map(int, input().split())
    fruits = list(map(int, input().split()))
    print(countFruitToEat(fruits, capacity))


if __name__ == "__main__":
    main()

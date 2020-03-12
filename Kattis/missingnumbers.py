def main():
    n = int(input())
    nums = set()
    for _ in range(n):
        num = int(input())
        nums.add(num)
        last_num = num
    if last_num == n:
        print("good job")
        return
    for i in range(1, last_num + 1):
        if i not in nums:
            print(i)


if __name__ == "__main__":
    main()

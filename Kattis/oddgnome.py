def main():
    T = int(input())
    for _ in range(T):
        nums = list(map(int, input().split()))
        for i in range(2, len(nums) - 1):
            if nums[i - 1] + 1 != nums[i]:
                print(i)
                break


if __name__ == "__main__":
    main()

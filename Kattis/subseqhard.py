T = int(input())
for _ in range(T):
    blank = input()
    N = int(input())
    nums = list(map(int, input().split()))
    sums = {0: 1}
    running_sum = 0
    count = 0
    for num in nums:
        running_sum += num
        count += sums.get(running_sum - 47, 0)
        sums[running_sum] = sums.get(running_sum, 0) + 1
    print(count)

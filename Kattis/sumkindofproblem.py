P = int(input())

for i in range(P):
    nums = input().split(' ')
    K, N = nums[0], int(nums[1])
    odd = N * 2

    s1 = N * (N + 1) / 2
    s2 = N ** 2
    s3 = s2 + N

    print(K, str(int(s1)), str(s2), str(s3))

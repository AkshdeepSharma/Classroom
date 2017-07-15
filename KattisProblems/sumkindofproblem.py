P = int(input())

for i in range(P):
    s1, s2, s3 = 0, 0, 0
    nums = input().split(' ')
    K = nums[0]
    N = int(nums[1])
    for positive in range(1, N + 1):
        s1 += positive

    for odd in range(1, N * 2, 2):
        s2 += odd

    for even in range(2, (N + 1) * 2, 2):
        s3 += even

    print(K, str(s1), str(s2), str(s3))

N = int(input())
qaly = 0
for i in range(N):
    nums = input().split(" ")
    qaly += float(nums[0]) * float(nums[1])
print(round(qaly, 3))

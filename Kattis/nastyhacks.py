N = int(input())
for _ in range(N):
    nums = list(map(int, input().split(" ")))
    if nums[0] + nums[2] < nums[1]:
        print("advertise")
    elif nums[0] + nums[2] > nums[1]:
        print("do not advertise")
    else:
        print("does not matter")

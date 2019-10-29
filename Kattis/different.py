try:
    while True:
        nums = input().split(' ')
        a = int(nums[0])
        b = int(nums[1])

        print(abs(a-b))
except EOFError:
    pass

num_bats = int(input())
bats_arr = map(int, input().split())
sum_bats = 0

for val in bats_arr:
    if val == -1:
        num_bats -= 1
    else:
        sum_bats += val
print(sum_bats / num_bats)
n = int(input().strip())
arr = [float(arr_temp) for arr_temp in input().strip().split(' ')]


for i in range(n):
    value = (arr[i] + 0.005505) / 0.274
    print(str(value))
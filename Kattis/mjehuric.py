def mjehuric(arr):
    sorted_arr = ["1", "2", "3", "4", "5"]
    res = []
    while sorted_arr != arr:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
            res.append(arr[:])
        if arr[1] > arr[2]:
            arr[1], arr[2] = arr[2], arr[1]
            res.append(arr[:])
        if arr[2] > arr[3]:
            arr[2], arr[3] = arr[3], arr[2]
            res.append(arr[:])
        if arr[3] > arr[4]:
            arr[3], arr[4] = arr[4], arr[3]
            res.append(arr[:])
    return res


def main():
    arr = input().split()
    res = mjehuric(arr)
    for i in range(len(res)):
        print(" ".join(res[i]))


if __name__ == "__main__":
    main()

def merge(left, right):
    res = []
    i, j = 0, 0
    inversions = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            inversions += len(left) - i
    res.extend(left[i:])
    res.extend(right[j:])
    return res, inversions

def count_inversions(arr):
    if len(arr) < 2:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    merged, inv_total = merge(left, right)
    inv_total += inv_left + inv_right
    return merged, inv_total

N = int(input())
student_numbers = [int(input()) for _ in range(N)]

print(count_inversions(student_numbers)[1])

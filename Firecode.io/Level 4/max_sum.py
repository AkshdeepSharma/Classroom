def largest_continuous_sum(arr):
    if not arr:
        return 0

    maxSum = currentSum = arr[0]

    for val in arr[1:]:
        currentSum = max(currentSum + val, val)
        maxSum = max(maxSum, currentSum)

    return maxSum

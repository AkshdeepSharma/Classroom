class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        running_sum = sum(arr[0:k])
        for i in range(len(arr) - k + 1):
            if i == 0:
                if running_sum / k >= threshold:
                    count += 1
                continue
            running_sum -= arr[i - 1]
            running_sum += arr[i + k - 1]
            if running_sum / k >= threshold:
                count += 1
        return count

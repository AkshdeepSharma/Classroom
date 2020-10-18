class Solution:
    def trimMean(self, arr: List[int]) -> float:
        five_percent = int(0.05 * len(arr))
        arr = sorted(arr)
        return sum(arr[five_percent:len(arr) - five_percent]) / (len(arr) - five_percent * 2)

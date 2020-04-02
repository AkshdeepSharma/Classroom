class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = [0] * 500
        for num in arr:
            count[num] += 1
        for i in reversed(range(1, len(count))):
            if count[i] == i:
                return i
        return -1

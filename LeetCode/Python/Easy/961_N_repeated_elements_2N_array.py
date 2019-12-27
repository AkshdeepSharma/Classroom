from collections import defaultdict
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        dic = defaultdict(int)
        for num in A:
            dic[num] += 1
            if dic[num] > 1:
                return num
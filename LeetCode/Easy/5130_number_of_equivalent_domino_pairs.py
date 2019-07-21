from collections import defaultdict
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        res = 0
        pairs = defaultdict(int)
        for pair in dominoes:
            temp = str(sorted(pair))
            pairs[temp] += 1
        for val in pairs.values():
            res += (val * (val - 1)) // 2
        return res
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_list = [0] * (N + 1)
        for a, b in trust:
            trust_list[a] -= 1
            trust_list[b] += 1

        for i in range(1, N + 1):
            if trust_list[i] == N - 1:
                return i
        return -1
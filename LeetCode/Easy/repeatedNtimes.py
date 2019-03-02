class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic = {}
        N = len(A) // 2
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key, val in dic.iteritems():
            if val == N:
                return key
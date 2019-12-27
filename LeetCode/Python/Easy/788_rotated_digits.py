class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1, N + 1):
            i_str = str(i)
            if '3' in i_str or '4' in i_str or '7' in i_str:
                continue
            if '2' in i_str or '5' in i_str or '6' in i_str or '9' in i_str:
                res += 1
        return res
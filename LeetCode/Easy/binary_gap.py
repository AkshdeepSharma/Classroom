class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N_bin = bin(N)[2:]
        if N_bin.count('1') == 1:
            return 0
        elif N_bin.count('0') == 0:
            return 1
        max_dist, curr = 0, 0
        for c in range(len(N_bin)):
            if N_bin[c] == '0':
                curr += 1
            else:
                curr += 1
                if curr > max_dist:
                    max_dist = curr
                curr = 0
        return max_dist
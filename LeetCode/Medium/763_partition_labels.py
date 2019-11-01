class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        right_letter = {}
        right, left = 0, 0
        res = []
        for i, char in enumerate(S):
            right_letter[char] = i

        for i, char in enumerate(S):
            right = max(right, right_letter[char])
            if right == i:
                res.append(right - left + 1)
                left = right + 1
        return res

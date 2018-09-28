class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        dic = {}
        for jewel in J:
            dic[jewel] = 1
        for stone in S:
            if stone in dic:
                count += 1
        return count

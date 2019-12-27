class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        count = 0
        res = [0] * num_people
        while candies > 0:
            res[count % num_people] += min(candies, count + 1)
            count += 1
            candies -= count
        return res
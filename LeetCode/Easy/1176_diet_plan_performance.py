class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        res = 0
        j = k
        for i in range(0, len(calories) - k + 1):
            if i == 0:
                k_cals = sum(calories[i:i+k])
            else:
                k_cals -= calories[i-1]
                k_cals += calories[i+k-1]
            if k_cals < lower:
                res -= 1
            elif k_cals > upper:
                res += 1
        return res
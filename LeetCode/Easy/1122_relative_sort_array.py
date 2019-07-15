class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {}
        not_in = []
        for num in arr2:
            if num not in dic:
                dic[num] = 0
        for num in arr1:
            if num in dic:
                dic[num] += 1
            else:
                not_in.append(num)
        for num in arr2:
            if dic[num] > 0:
                while dic[num] != 0:
                    res.append(num)
                    dic[num] -= 1
        return res + sorted(not_in)
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curr_number = arr[0]
        frequency = 0
        for num in arr:
            if num == curr_number:
                frequency += 1
                if frequency / len(arr) > 0.25:
                    return curr_number
            else:
                curr_number = num
                frequency = 1

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0: return intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        
        for i, currI in enumerate(intervals):
            lastI = res[-1]
            if currI[0] <= lastI[-1]:
                lastI[-1] = max(currI[1], lastI[-1])
            else:
                res.append(currI)
        return res
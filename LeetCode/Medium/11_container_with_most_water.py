class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            curr = min(height[left], height[right]) * (right - left)
            if curr > best:
                best = curr
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
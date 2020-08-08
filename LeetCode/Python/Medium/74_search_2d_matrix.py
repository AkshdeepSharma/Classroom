class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchRow(row, target):
            lo, hi = 0, len(row) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] < target:
                    lo = mid + 1
                elif row[mid] > target:
                    hi = mid - 1
                else:
                    return True
            return False

        if not matrix or not matrix[0] or matrix[-1][-1] < target:
            return False
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                break
        return binarySearchRow(matrix[i], target)

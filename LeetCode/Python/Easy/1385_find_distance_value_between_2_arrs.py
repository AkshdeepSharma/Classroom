class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance_value = 0
        for num1 in arr1:
            valid = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    valid = False
                    break
            if valid:
                distance_value += 1
        return distance_value
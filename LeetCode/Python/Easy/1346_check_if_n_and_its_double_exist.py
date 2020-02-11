class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_arr = set(arr)
        if arr.count(0) >= 2:
            return True
        set_arr.discard(0)
        for num in arr:
            if num * 2 in set_arr or (num % 2 == 0 and num // 2 in set_arr):
                return True
        return False

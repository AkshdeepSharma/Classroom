class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        best_zero, current_zero, best_one, current_one = 0, 0, 0, 0
        for num in s:
            if num == '1':
                current_zero = 0
                current_one += 1
            else:
                current_zero += 1
                current_one = 0
            best_zero = max(best_zero, current_zero)
            best_one = max(best_one, current_one)
        return best_one > best_zero

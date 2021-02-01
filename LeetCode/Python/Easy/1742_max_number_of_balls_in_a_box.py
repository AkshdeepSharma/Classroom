class Solution:
    def countBalls(self, low_limit: int, high_limit: int) -> int:
        count = {}
        for i in range(low_limit, high_limit + 1):
            sum_of_digits = sum(map(int, list(str(i))))
            if sum_of_digits not in count:
                count[sum_of_digits] = 0
            count[sum_of_digits] += 1
        return count[max(count, key=count.get)]

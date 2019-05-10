class Solution:
    def reverse(self, x: int) -> int:
        y = list(str(x))[::-1]
        if len(y) == 1:
            return int(''.join(y))
        if y[-1] == '-':
            to_insert = y.pop()
            y.insert(0, to_insert)
        elif y[0] == '0':
            y.pop(0)
        y = int(''.join(y))
        if -2 ** 31 > y or y > (2 ** 31) - 1:
            return 0
        return y

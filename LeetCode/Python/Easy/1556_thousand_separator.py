class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = []
        temp = ''
        i = 0
        if n == 0:
            return '0'
        while n:
            i += 1
            temp = str(n % 10) + temp
            n //= 10
            if i % 3 == 0:
                ans.append(temp)
                temp = ''
        ans = ".".join(ans[::-1])
        if temp and ans:
            return temp + "." + ans
        if temp:
            return temp
        return ans
# ugly code imo

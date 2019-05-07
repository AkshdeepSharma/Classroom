class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = sign = ""
        if num < 0:
            sign = "-"
            num *= -1
        while num >= 7:
            remainder = num % 7
            num //= 7
            res += str(remainder)
        res += str(num)
        res = res[::-1]
        if sign == "-":
            res = str(int(res) * -1)
        return res
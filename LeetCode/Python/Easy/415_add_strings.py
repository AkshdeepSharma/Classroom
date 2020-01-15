class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry, res = 0, []
        while num1 or num2:
            if num1:
                n1 = ord(num1.pop()) - ord('0')
            else:
                n1 = 0
            if num2:
                n2 = ord(num2.pop()) - ord('0')
            else:
                n2 = 0
            summed = n1 + n2 + carry
            carry = summed // 10
            res.append(str(summed % 10))
        if carry:
            res.append(str(carry))
        return "".join(res)[::-1]

        # return int(num1) + int(num2)

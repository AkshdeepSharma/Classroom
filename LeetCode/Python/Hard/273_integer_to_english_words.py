class Solution:
    def numberToWords(self, num: int) -> str:
        lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                      "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000, lessThan20,
                                  tens) + thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num, lessThan20, tens):
        if num == 0:
            return ""
        if num < 20:
            return lessThan20[num] + " "
        if num < 100:
            return tens[num // 10] + " " + self.helper(num % 10, lessThan20, tens)
        return lessThan20[num // 100] + " Hundred " + self.helper(num % 100, lessThan20, tens)

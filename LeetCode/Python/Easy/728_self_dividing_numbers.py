class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            num = str(i)
            if '0' in num:
                pass
            else:
                for j in range(len(num)):
                    if int(num) % int(num[j]) != 0:
                        break
                    elif j == len(num) - 1 and int(num) % int(num[j]) == 0:
                        res.append(int(num))
        return res
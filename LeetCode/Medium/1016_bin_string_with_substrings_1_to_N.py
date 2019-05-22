class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N + 1):
            binary = bin(i)[2:]
            if binary not in S:
                return False
        return True
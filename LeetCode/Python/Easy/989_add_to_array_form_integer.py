class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return map(int, list(str(int("".join(map(str, A))) + K)))

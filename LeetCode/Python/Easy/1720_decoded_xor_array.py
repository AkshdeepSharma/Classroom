class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        original = [first]
        for num in encoded:
            original.append(original[-1] ^ num)
        return original

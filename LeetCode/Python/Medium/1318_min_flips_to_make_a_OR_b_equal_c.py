class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flipped_bits = 0
        a, b, c = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        largest_length = max(len(a), len(b), len(c))
        a, b, c = (largest_length - len(a)) * '0' + a, (largest_length -
                                                        len(b)) * '0' + b, (largest_length - len(c)) * '0' + c

        for i in reversed(range(len(c))):
            if c[i] == '0':
                if a[i] == '1':
                    flipped_bits += 1
                if b[i] == '1':
                    flipped_bits += 1
            elif c[i] == '1':
                if a[i] == '0' and b[i] == '0':
                    flipped_bits += 1
        return flipped_bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = 0

        one = 1
        while n:
            bits += n & one
            n >>= 1
        return bits
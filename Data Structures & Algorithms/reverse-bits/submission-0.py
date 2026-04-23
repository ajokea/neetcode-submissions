class Solution:
    def reverseBits(self, n: int) -> int:
        num = 0
        bit = 2 ** 31

        while n:
            num += (n & 1) * bit
            n >>= 1
            bit >>= 1
        
        return num
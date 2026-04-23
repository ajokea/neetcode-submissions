class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for num in range(n + 1):
            bits = 0
            while num:
                bits += num & 1
                num >>= 1
            output.append(bits)
        return output
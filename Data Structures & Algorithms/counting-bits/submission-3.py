class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0 for _ in range(n + 1)]

        offset = 1
        for i in range(1, n + 1):
            if i == offset << 1:
                offset = i
            bits[i] = 1 + bits[i - offset]

        return bits
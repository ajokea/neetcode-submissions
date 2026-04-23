class Solution:
    def countBits(self, n: int) -> List[int]:
        table = [0 for _ in range(n + 1)]

        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset <<= 1
            table[i] = 1 + table[i - offset]

        return table
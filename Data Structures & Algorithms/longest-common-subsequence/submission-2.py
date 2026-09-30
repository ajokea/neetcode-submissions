class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # if len(text1) == 0 or len(text2) == 0:
        #     return 0

        # if text1[0] == text2[0]:
        #     return 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        # else:
        #     return max(
        #         self.longestCommonSubsequence(text1, text2[1:]),
        #         self.longestCommonSubsequence(text1[1:], text2))

        table = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    table[i][j] = 1 + table[i-1][j-1]
                else:
                    table[i][j] = max(table[i-1][j], table[i][j-1])

        return table[-1][-1]

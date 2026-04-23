class Solution:
    def numDecodings(self, s: str) -> int:
        table = [0 for _ in range(len(s) + 1)]

        table[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] != "0":
                table[i] = table[i + 1]
                if (
                    i + 2 <= len(s) and 
                    (s[i] == "1" or 
                    (s[i] == "2" and s[i + 1] in "0123456"))):
                    table[i] += table[i + 2]

        return table[0]
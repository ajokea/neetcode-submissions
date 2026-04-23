class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        table = [False for _ in range(len(s) + 1)]
        table[-1] = True

        for i in range(len(s) - 1, -1 , -1):
            for word in wordDict:
                if ((i + len(word)) <= len(s) 
                    and s[i : i + len(word)] == word):
                    table[i] = table[i + len(word)]
                    if table[i]:
                        break

        return table[0]
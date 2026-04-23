class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLength = 0

        for i in range(len(s)):
            # find odd palindromes
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLength:
                    result = s[l : r + 1]
                    resultLength = r - l + 1
                l -= 1
                r += 1

            # find even palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLength:
                    result = s[l : r + 1]
                    resultLength = r - l + 1
                l -= 1
                r += 1
        
        return result
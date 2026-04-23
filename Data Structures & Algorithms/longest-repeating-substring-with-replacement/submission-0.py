class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1

        charMap = {}
        l = 0
        for r in range(len(s)):
            charMap[s[r]] = charMap.get(s[r], 0) + 1

            while (r - l + 1) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
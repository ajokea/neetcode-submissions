class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        l = r = 0
        charSet = set()
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])
            r += 1
            longest = max(longest, r - l)
        
        return longest
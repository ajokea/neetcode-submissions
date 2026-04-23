class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Chars, s2Chars = {}, {}
        for char in s1:
            if char not in s1Chars:
                s1Chars[char] = 0
                s2Chars[char] = 0
            s1Chars[char] += 1

        l = 0
        for r in range(len(s2)):
            char = s2[r]
            if char not in s1Chars:
                while l <= r:
                    l += 1
                s2Chars = {}
            else:
                s2Chars[char] = s2Chars.get(char, 0) + 1
                while s2Chars[char] > s1Chars[char]:
                    s2Chars[s2[l]] -= 1
                    l += 1
                if s1Chars == s2Chars:
                    return True
        return False
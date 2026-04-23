class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(char):
            return (ord('a') <= ord(char.lower()) <= ord('z')) or (ord('0') <= ord(char) <= ord('9'))

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not isAlphaNum(s[l]):
                l += 1
            
            while l < r and not isAlphaNum(s[r]):
                r -= 1
            
            if l > r or s[l].lower() != s[r].lower():
                print(l, r)
                return False
            
            l += 1
            r -= 1
        return True

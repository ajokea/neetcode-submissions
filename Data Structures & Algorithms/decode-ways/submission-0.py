class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        
        # a string starting with zero cannot be decoded
        if s[0] == "0":
            return 0

        # any other digit is valid for a string of length 1
        result = self.numDecodings(s[1:])
        # a valid character can be from 1 to 26
        if (1 in range(len(s))) and (s[0] == "1" or (s[0] == "2" and s[1] in "0123456")):
            result += self.numDecodings(s[2:])
        
        return result
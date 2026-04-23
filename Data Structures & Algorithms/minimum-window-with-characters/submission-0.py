class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""

        result = ""
        resultLength = float('inf')

        tMap, window = {}, {}
        need = 0
        for char in t:
            if char not in tMap:
                need += 1
                window[char] = 0
            tMap[char] = tMap.get(char, 0) + 1

        l = 0
        have = 0
        for r in range(len(s)):
            if s[r] not in tMap and have == 0:
                l += 1
                continue

            if s[r] in tMap:
                window[s[r]] += 1          
            
                if window.get(s[r]) == tMap.get(s[r]):
                    have += 1
                    
                while have == need:
                    length = r - l + 1
                    if length < resultLength:
                        result = s[l:r+1]
                        resultLength = length
                    
                    if s[l] in tMap:
                        window[s[l]] -= 1
                        if window.get(s[l]) < tMap.get(s[l]):
                            have -= 1
                        
                    l += 1
        return result
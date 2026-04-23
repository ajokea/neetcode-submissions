class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""

        result = [-1,-1]
        resultLength = float('inf')

        tMap, window = {}, {}
        need = 0
        for char in t:
            if char not in tMap:
                need += 1
            tMap[char] = tMap.get(char, 0) + 1

        l = 0
        have = 0
        for r in range(len(s)):
            if s[r] not in tMap and have == 0:
                l += 1
                continue

            window[s[r]] = window.get(s[r], 0) + 1         
            
            if window.get(s[r]) == tMap.get(s[r]):
                have += 1
                    
            while have == need:
                length = r - l + 1
                if length < resultLength:
                    result = [l,r]
                    resultLength = length
                    
                if s[l] in tMap:
                    window[s[l]] -= 1
                    if window.get(s[l]) < tMap.get(s[l]):
                        have -= 1
                        
                l += 1
        l, r = result
        return s[l:r+1] if resultLength != float('inf') else ""
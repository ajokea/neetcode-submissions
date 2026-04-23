class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = [-1, -1]
        resultLength = float('inf')

        tMap = {}
        need = 0 # chars needed in t string
        for char in t:
            if char not in tMap:
                tMap[char] = 1
                need += 1
            else:
                tMap[char] += 1
        
        window = {}
        have = 0 # chars we have in the window from chars needed

        l = 0
        for r in range(len(s)):
            if s[r] in tMap:
                window[s[r]] = window.get(s[r], 0) + 1
                
                if window[s[r]] == tMap[s[r]]:
                    have += 1

                    while have == need:
                        if (r - l + 1) < resultLength:
                            result = [l, r]
                            resultLength = r - l + 1
                        
                        if s[l] in tMap:
                            window[s[l]] -= 1
                            if window[s[l]] < tMap[s[l]]:
                                have -= 1
                        
                        l += 1
            else:
                if not window:
                    l += 1
        
        l, r = result
        return s[l:r + 1] if resultLength != float('inf') else ""

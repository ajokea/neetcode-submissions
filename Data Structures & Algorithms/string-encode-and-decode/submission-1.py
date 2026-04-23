class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for i in range(len(strs)): 
            code = str(len(strs[i])) + '%'
            encoded += code + strs[i]
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '%':
                j += 1
            wordLength = int(s[i:j])
            i = j + 1
            j = i + wordLength
            decoded.append(s[i:j])
            i = j
        
        return decoded
        
    
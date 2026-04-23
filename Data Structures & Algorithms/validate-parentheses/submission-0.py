class Solution:
    def isValid(self, s: str) -> bool:        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        return True
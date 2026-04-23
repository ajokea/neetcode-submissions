class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(opened, closed, combo):
            if opened == closed == n:
                result.append("".join(combo[:]))
                return
            
            # we can only add an opened parenthese if opened < n
            if opened < n:
                combo.append("(")
                helper(opened + 1, closed, combo)
                combo.pop()
            # we can only add a closed parenthese if closed < opened
            if closed < opened:
                combo.append(")")
                helper(opened, closed + 1, combo)
                combo.pop()

        helper(0, 0, [])
        return result
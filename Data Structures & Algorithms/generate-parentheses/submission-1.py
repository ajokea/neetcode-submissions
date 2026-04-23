class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(opened, closed, stack):
            if opened == closed == n:
                result.append("".join(stack))
                return
            
            # we can only add an opened parenthese if opened < n
            if opened < n:
                stack.append("(")
                helper(opened + 1, closed, stack)
                stack.pop()
            # we can only add a closed parenthese if closed < opened
            if closed < opened:
                stack.append(")")
                helper(opened, closed + 1, stack)
                stack.pop()

        helper(0, 0, [])
        return result
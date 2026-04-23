class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def helper(i, part):
            if i == len(s):
                result.append(part[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i : j + 1])
                    helper(j + 1, part)
                    part.pop()

        helper(0, [])
        return result

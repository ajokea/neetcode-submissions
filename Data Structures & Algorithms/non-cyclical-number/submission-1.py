class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSum(num):
            result = 0
            while num:
                result += (num % 10) ** 2
                num //= 10
            return result
        
        seen = set()
        while n != 1:
            n = digitSum(n)
            if n in seen:
                return False
            seen.add(n)
        return True
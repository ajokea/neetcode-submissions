class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = currentOnes = 0

        for num in nums:
            if num == 1:
                currentOnes += 1
            else:
                currentOnes = 0
                
            maxOnes = max(currentOnes, maxOnes)

        return maxOnes
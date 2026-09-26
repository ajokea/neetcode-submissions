class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = set()
        for num in nums:
            if num in counts:
                return True
            counts.add(num)
        return False
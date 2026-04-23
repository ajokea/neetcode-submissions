class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        
        product = 1
        for num in nums:
            output.append(product)
            product *= num
        
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= product
            product *= nums[i]
        
        return output
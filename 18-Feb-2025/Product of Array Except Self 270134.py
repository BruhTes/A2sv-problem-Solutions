# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for i in range(len(nums))]

        prefix = 1
        for i in range(len(result)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(result) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
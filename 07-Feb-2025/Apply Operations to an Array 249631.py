# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Step 1: Combine adjacent equal elements
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 2  # Skip the next element after combining
            else:
                i += 1
        
        # Step 2: Move all zeros to the end
        non_zero_pos = 0  # Position to place the next non-zero element
        for num in nums:
            if num != 0:
                nums[non_zero_pos] = num
                non_zero_pos += 1
        
        # Step 3: Fill the remaining positions with zeros
        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0
        
        return nums

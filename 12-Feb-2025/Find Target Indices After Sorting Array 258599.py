# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        count_above = 0
        count_below = 0
        indices = []

        for num in nums:
            if num > target:
                count_above += 1
            elif num < target:
                count_below += 1
        
        indices.extend(range(count_below, len(nums) - count_above))
        
        return indices

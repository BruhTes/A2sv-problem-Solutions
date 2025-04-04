# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        i = 0

        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                if nums[i] == nums[nums[i] - 1]:
                    result.add(nums[i])
                    i += 1
                else:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                
    
        return list(result)
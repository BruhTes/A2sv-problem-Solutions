# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for num, i in enumerate(nums):
            if num != i:
                return i - 1
        
        return len(nums)
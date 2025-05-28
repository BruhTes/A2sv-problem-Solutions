# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        left = 0
        right = n - 1
        while left < right: 
            if nums[left] <= nums[left + 1]:
                left += 1
                continue
            if nums[right - 1] <= nums[right]:
                right -= 1
                continue
            if left + 1 != right:
                return False     
            if left == 0 or right == n - 1:
                return True
            return nums[left] <= nums[right + 1] or nums[left - 1] <= nums[right]
        return True
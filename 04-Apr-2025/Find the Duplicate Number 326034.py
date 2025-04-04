# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        acc = set()
        for i in range(len(nums)):
            if nums[i] in acc:
                return nums[i]
            else:
                acc.add(nums[i])
        
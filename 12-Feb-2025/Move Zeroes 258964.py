# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = -1

        for p2 in range(len(nums)):
            if nums[p2] != 0:
                # nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
        return nums
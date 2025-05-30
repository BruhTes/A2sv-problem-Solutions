# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def flip(start, end, nums):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # incase k > len(nums)
        k = k % len(nums)
        
        flip(0, len(nums) - 1, nums)
        flip(0, k - 1, nums)
        flip(k, len(nums) - 1, nums)

        return nums
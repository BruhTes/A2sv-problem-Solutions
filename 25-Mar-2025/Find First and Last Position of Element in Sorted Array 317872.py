# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(foo):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= foo:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        
        first = search(target)
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        
        last = search(target + 1) - 1
        return [first, last]

# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        count = 0
        
        left_bound = -1
        last_min = -1
        last_max = -1
        
        for i in range(n):
            
            if nums[i] < minK or nums[i] > maxK:
                left_bound = i
            
            if nums[i] == minK:
                last_min = i
            if nums[i] == maxK:
                last_max = i
            
            if last_min > left_bound and last_max > left_bound:
                count += min(last_min, last_max) - left_bound
        
        return count
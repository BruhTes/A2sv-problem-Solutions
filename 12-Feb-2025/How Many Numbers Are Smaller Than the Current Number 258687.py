# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        smaller_counter = {}
        for i, num in enumerate(sorted_nums):
            if num not in smaller_counter:
                smaller_counter[num] = i
        
        return [smaller_counter[num] for num in nums]
# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        zeroCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        
        left = 0
        right = k
        current_sum = max_sum

        while right < len(nums):
            current_sum += nums[right] - nums[left]
            max_sum = max(current_sum, max_sum)

            left += 1
            right += 1
        
        return max_sum / k
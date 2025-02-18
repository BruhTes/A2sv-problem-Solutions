# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minPrefixSum = 0
        maxPrefixSum = float('-inf')
        prefixSum = 0

        for num in nums:
            prefixSum += num
            
            maxPrefixSum = max(maxPrefixSum, prefixSum - minPrefixSum)
            minPrefixSum = min(minPrefixSum, prefixSum)
            
        return maxPrefixSum
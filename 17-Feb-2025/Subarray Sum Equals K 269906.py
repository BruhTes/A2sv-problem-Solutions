# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freqMap = {0 : 1}
        count = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num

            if prefixSum - k in freqMap:
                count += freqMap[prefixSum - k]
            
            freqMap[prefixSum] = freqMap.get(prefixSum, 0) + 1
        
        return count
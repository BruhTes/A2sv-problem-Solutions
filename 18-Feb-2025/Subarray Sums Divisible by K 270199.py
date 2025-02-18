# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        subArrays = {0 : 1}
        count = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num

            if prefixSum % k in subArrays:
                count += subArrays[prefixSum % k]
            
            subArrays[prefixSum % k] = subArrays.get(prefixSum % k, 0) + 1
        
        return count
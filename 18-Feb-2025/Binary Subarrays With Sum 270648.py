# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        counter = {0 : 1}
        prefixSum = 0

        for num in nums:
            prefixSum += num

            if prefixSum - goal in counter:
                count += counter[prefixSum - goal]
            
            counter[prefixSum] = counter.get(prefixSum, 0) + 1
        
        return count
# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = 0
        indexMap = {0 : -1}
        max_len = 0

        for i, num in enumerate(nums):
            prefixSum += 1 if num == 1 else -1

            if prefixSum in indexMap:
                max_len = max(max_len, i - indexMap[prefixSum])
            else:
                indexMap[prefixSum] = i
        
        return max_len
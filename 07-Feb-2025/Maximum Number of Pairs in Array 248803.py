# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        nums = Counter(nums)
        removed = 0
        leftover = 0

        for key in nums:
            removed += nums[key] // 2
            leftover += nums[key] % 2

        return [removed, leftover]
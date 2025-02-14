# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        def compare(a, b):
            if a + b > b + a:
                return -1
            return 1
        
        nums = sorted(nums, key = cmp_to_key(compare))

        return str(int("".join(nums)))
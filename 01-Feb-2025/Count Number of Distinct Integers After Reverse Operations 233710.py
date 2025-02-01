# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for num in nums:
            digit = 0
            while num > 0:
                digit = digit * 10 + num % 10
                num //= 10
            nums_set.add(digit)
        return len(nums_set)
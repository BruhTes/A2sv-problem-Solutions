# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        unique = set()
        result = []

        for num in nums:
            if num in unique:
                result.append(num)
            else:
                unique.add(num)
        return result
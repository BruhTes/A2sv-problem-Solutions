# Problem: Concatenation of Array - https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums
        nums.extend(nums2)
        return nums
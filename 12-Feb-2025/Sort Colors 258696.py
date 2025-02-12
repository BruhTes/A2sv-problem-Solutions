# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0 for i in range(3)]
        for num in nums:
            counter[num] += 1
            
        index = 0
        for i in range(3):
            for _ in range(counter[i]):
                nums[index] = i
                index += 1
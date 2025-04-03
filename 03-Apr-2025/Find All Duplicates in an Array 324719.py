# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        tracker = [0] * len(nums)
        duplicates = []

        for num in nums:
            index = num - 1

            if tracker[index] == 1:
                duplicates.append(num)
            else:
                tracker[index] = 1
        
        return duplicates
# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for i in range(len(nums)):
            new = []

            for subset in ans:
                new.append(subset + [nums[i]])
            
            ans += new
        
        return ans
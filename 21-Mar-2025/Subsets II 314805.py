# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()
        
        def backtrack(path, index):
            if path not in subsets:
                subsets.append(path[:])
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()
            
        backtrack([], 0)
        return subsets
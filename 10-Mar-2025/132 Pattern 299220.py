# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums_k = float('-inf') # for nums[k]
        stack = []  # to track nums[j]

        for i in range(len(nums) - 1, - 1, -1):
            if nums[i] < nums_k:
                return True

            while stack and stack[-1] < nums[i]:
                nums_k = stack.pop()
            
            stack.append(nums[i])
        return False
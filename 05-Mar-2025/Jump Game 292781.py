# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0: return True

        aimedIdx = len(nums) - 1
        i = len(nums) - 2

        while i >= 0:
            if aimedIdx - i <= nums[i]:
                aimedIdx = i
            i -= 1
        return aimedIdx == 0
# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, seen):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if i not in seen:
                    path.append(nums[i])
                    seen.add(i)
                    backtrack(path, seen)
                    path.pop()
                    seen.remove(i)

        backtrack([], set())
        return result

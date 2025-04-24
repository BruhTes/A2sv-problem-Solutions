# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = [0, 0]

        for i in range(1, len(nums) + 1):
            if counter[i] == 0:
                result[1] = i
            if counter[i] == 2:
                result[0] = i
        
        return result
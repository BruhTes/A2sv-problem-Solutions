# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)

        div_sum = [right_sum]

        for i in range(len(nums)):
            if nums[i] == 0:
                left_sum += 1
            else:
                right_sum -= 1
            
            div_sum.append(left_sum + right_sum)
        
        max_sum = max(div_sum)
        
        return [idx for idx, score in enumerate(div_sum) if score == max_sum]

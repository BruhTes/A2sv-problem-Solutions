# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right):
            if left == right:
                return nums[left]
            
            pick_left = nums[left] - predict(left + 1, right)
            pick_right = nums[right] - predict(left, right - 1)
            
            return max(pick_left, pick_right)
        
        return predict(0, len(nums) - 1) >= 0

# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = 0
        min_dif = float('inf')
        
        print(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return target
                elif current_sum > target:
                    right -= 1
                else:
                    left += 1
                
                if min_dif > abs(target - current_sum):
                    min_dif = abs(target - current_sum)
                    closest_sum = current_sum
        
        return closest_sum
            

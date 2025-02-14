# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.append((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        
        return list(set(triplets))

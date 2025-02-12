# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indices = []
        nums.sort()

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1
            
            else:
                left = mid
                right = mid 

                while left >= 0 and nums[left] == target:
                    left -= 1
                while right <= len(nums) - 1 and nums[right] == target:
                    right += 1
                
                indices.extend(range(left + 1, right))
                break
        
        return indices
# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        def first_occ(nums, target):
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right -= 1
                else:
                    left += 1

            return first
        
        def last_occ(nums, target):
            left, right = 0, len(nums) - 1
            last = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last = mid
                    left += 1
                elif nums[mid] > target:
                    right -= 1
                else:
                    left += 1

            return last
        
        nums.sort()
        a = first_occ(nums, target)
        b = last_occ(nums, target)
        print(a, b)

        return list(range(a, b + 1)) if a + b >= 0 else []
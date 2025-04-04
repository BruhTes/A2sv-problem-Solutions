# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        def mergeSort(left, right):
            if left == right:
                return [(nums[left], left)]

            mid = left + (right - left) // 2
            left_sorted = mergeSort(left, mid)
            right_sorted = mergeSort(mid + 1, right)

            return merge(left_sorted, right_sorted)
        
        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) and j < len(right):
                if left[i][0] <= right[j][0]:
                    merged.append(left[i])
                    result[left[i][1]] += right_count
                    i += 1
                else:
                    merged.append(right[j])
                    right_count += 1
                    j += 1
            
            # merged.extend(left[i:])
            while i < len(left):
                result[left[i][1]] += right_count
                merged.append(left[i])
                i += 1
            
            merged.extend(right[j:])

            return merged
        
        mergeSort(0, len(nums) - 1)
        return result
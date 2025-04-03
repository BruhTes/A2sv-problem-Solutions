# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(x):
            subarray_count = 0
            current_sum = 0

            for num in nums:
                current_sum += num

                if current_sum > x:
                    subarray_count += 1
                    current_sum = num
                
                if subarray_count + 1 > k:
                    return False
            return True
        
        low, high = max(nums), sum(nums)
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2

            if canSplit(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
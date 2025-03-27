# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def canFormZeroArray(k):
            diff = [0] * n
            for i in range(k + 1):
                left, right, val = queries[i]
                diff[left] -= val
                if right < n - 1:
                    diff[right + 1] += val
            
            prefix_sum = 0
            for i in range(n):
                prefix_sum += diff[i]
                if prefix_sum + nums[i] > 0:
                    return False
            return True
        
        if all(num == 0 for num in nums):
            return 0
            
        left = 0
        right = len(queries) - 1
        ans = -1

        while right >= left:
            mid = left + (right - left) // 2
            if canFormZeroArray(mid):
                ans = mid + 1
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
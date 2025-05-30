# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums):
        min_prefix_sum = float("inf")
        max_prefix_sum = float("-inf")
        prefix_sum = 0
        max_abs_sum = 0

        for num in nums:
            prefix_sum += num

            min_prefix_sum = min(min_prefix_sum, prefix_sum)
            max_prefix_sum = max(max_prefix_sum, prefix_sum)

            if prefix_sum >= 0:
                max_abs_sum = max(
                    max_abs_sum, max(prefix_sum, prefix_sum - min_prefix_sum)
                )
            elif prefix_sum <= 0:
                max_abs_sum = max(
                    max_abs_sum,
                    max(abs(prefix_sum), abs(prefix_sum - max_prefix_sum)),
                )

        return max_abs_sum
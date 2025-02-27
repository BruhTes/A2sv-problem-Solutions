# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_prefix_sum = [0] * (n + 1)
        odd_prefix_sum = [0] * (n + 1)
        
        even_sum = 0
        odd_sum = 0
        
        for i in range(n):
            if i % 2 == 0:
                even_sum += nums[i]
            else:
                odd_sum += nums[i]
                
            even_prefix_sum[i + 1] = even_sum
            odd_prefix_sum[i + 1] = odd_sum
        
        valid_ways = 0
        for i in range(n):
        
            remaining_even_sum = even_prefix_sum[i] + (odd_prefix_sum[-1] - odd_prefix_sum[i + 1])
            remaining_odd_sum = odd_prefix_sum[i] + (even_prefix_sum[-1] - even_prefix_sum[i + 1])
            
            if remaining_even_sum == remaining_odd_sum:
                valid_ways += 1
        
        return valid_ways

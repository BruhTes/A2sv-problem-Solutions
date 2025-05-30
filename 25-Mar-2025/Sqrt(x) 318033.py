# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            if mid ** 2 <= x:
                sqrt = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return sqrt
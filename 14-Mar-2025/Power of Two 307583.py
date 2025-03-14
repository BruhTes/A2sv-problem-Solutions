# Problem: Power of Two - https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def power(n):
            if n == 1:
                return True
            if n % 2 != 0:
                return False
            return power(n // 2)
        
        return power(n)
# Problem: Power of Three - https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        def power(n):
            if n == 1:
                return True
            if n % 3 != 0:
                return False
            
            return power(n // 3)
        
        return power(n)
# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif left**2 + right**2 > c:
                right -= 1
            else:
                left += 1
        
        return False
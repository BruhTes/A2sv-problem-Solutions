# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = 0
        
        # did the first transformation with the conversion
        for char in s:
            value = ord(char) - ord("a") + 1
            while value > 0:
                result += value%10
                value //= 10
        
        
        # did k - 1 iterations since the first iteration is done already
        for _ in range(1, k):
            current_sum = 0

            while result > 0:
                current_sum += result % 10
                result //= 10
            
            result = current_sum

            if result < 10:
                return result
        return result
        
 
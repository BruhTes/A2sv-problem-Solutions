# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        original = x

        while (x > 0):
            temp = x % 10
            reverse = reverse*10 + temp
            x //= 10
            print(temp, x)
        
        return original == reverse
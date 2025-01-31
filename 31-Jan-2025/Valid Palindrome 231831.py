# Problem: Valid Palindrome - https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted = ""

        for char in s:
            if char.isalnum():
                converted += char.lower()
        
        return converted == converted[::-1]

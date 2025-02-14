# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                delLeft = s[left + 1 : right + 1]
                delRight = s[left : right]
                return delLeft == delLeft[::-1] or delRight == delRight[::-1]

            left, right = left + 1, right - 1
        return True
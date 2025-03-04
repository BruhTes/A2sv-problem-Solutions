# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for char in s:
            balance += 1 if char == 'R' else -1

            if not balance:
                count += 1
            
        return count
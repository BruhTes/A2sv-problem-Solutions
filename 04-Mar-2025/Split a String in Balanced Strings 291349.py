# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lcount = 0
        rcount = 0
        count = 0

        for char in s:
            if char == 'R':
                rcount += 1
            else:
                lcount += 1
            
            if lcount == rcount:
                count += 1
                lcount = 0
                rcount = 0
        return count 
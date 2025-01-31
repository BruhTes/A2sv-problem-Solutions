# Problem: Rotate String - https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       
       if len(s) != len(goal):
            return False
       concat = s + s
       
       return concat.find(goal) != -1
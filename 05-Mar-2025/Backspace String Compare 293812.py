# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []

        for char in s:
            if char != "#":
                stackS.append(char)
            else:
                if stackS:
                    stackS.pop()

        for char in t:
            if char != "#":
                stackT.append(char)
            else:
                if stackT:
                    stackT.pop()
        
        return stackS == stackT

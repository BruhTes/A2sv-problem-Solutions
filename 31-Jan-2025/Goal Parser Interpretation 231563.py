# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        result = ""

        while i < len(command):
            if command[i] == "G":
                result += "G"
                i += 1
            elif command[i : i + 2] == "()":
                result += "o"
                i += 2
            else:
                result += "al"
                i += 4
        
        return result
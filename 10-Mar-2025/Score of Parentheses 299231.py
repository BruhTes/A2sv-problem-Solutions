# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0

        for i, char in enumerate(s):
            if char == "(":
                depth += 1
            else:
                depth -= 1
            
                if s[i - 1] == "(" and i != 0:
                    score += (2 ** depth)
            
        return score

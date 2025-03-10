# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
    
        for char in s:
            if char == "(":
                stack.append(char)
            else:
                top = stack.pop()

                if top == "(":
                    stack.append(1)
                else:
                    score = 0
                    while top != "(":
                        score += top
                        top = stack.pop()
                    stack.append(2 * score)

        return sum(stack)
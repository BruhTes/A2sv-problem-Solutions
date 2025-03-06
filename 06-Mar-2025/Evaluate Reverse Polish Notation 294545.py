# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        expressions = {'+', '-', '*', '/'}

        for char in tokens:
            if char in expressions:
                a = stack.pop()
                b = stack.pop()
                if char == '+':
                    stack.append(b + a)
                elif char == '-':
                    stack.append(b - a)
                elif char == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(char))
        return stack[0]
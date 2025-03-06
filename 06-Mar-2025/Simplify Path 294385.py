# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        stack = []
        elements = path.split('/')
        print(elements)
        
        for element in elements:
            if element == '.' or element == '':
                continue
            
            if element == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(element)
        return '/' + '/'.join(stack)
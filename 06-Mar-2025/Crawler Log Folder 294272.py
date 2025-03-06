# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for char in logs:
            if char != "../" and char != "./":
                stack.append(char)
            else:
                if stack and char == "../":
                    stack.pop()
        
        return len(stack)
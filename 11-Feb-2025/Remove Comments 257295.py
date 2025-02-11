# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        output = []
        block = False

        clean_line = ""
        for line in source:
            i = 0

            while i < len(line):
                if block:
                    if i+1 < len(line) and line[i] == '*' and line[i+1] == '/':
                        block = False
                        i += 1
                else:
                    if i+1 < len(line) and line[i] == '/' and line[i+1] == '*':
                        block = True
                        i += 1
                    elif i+1 < len(line) and line[i] == '/' and line[i+1] == '/':
                        break
                    else:
                        clean_line += line[i]
                i += 1
            if not block and clean_line:
                output.append(clean_line)
                clean_line = ""
        return output
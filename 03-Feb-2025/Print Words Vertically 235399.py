# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        max_len : int = max([len(word) for word in s])
        
        vertical : list[str] = []
        for i in range(max_len):
            current_str : str = ""

            for word in s:
                if i > len(word) - 1:
                    current_str += " "
                else:
                    current_str += word[i]

            vertical.append(current_str.rstrip())

        return vertical
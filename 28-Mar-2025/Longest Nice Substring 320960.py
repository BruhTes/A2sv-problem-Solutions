# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def divide(string):
            if len(string) <= 1:
                return ""
            set_ = set(string)
            for i, char in enumerate(string):
                opp = char.swapcase()
                if opp not in set_:
                    left = divide(string[:i])
                    right = divide(string[i + 1:])
                    if len(left) >= len(right):
                        return left
                    return right
            return string
        
        return divide(s)
# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_space = len(s) - 1

        while (s[last_space] == " "):
            last_space -= 1
        
        counter = 0
        while (s[last_space] != " " and last_space > -1):
            counter += 1
            last_space -= 1
        
        return counter
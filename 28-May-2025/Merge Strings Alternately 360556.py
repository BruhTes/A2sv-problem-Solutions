# Problem: Merge Strings Alternately - https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        l, r = 0, 0

        while( l + r < len(word1) + len(word2)):
            if l < len(word1):
                result += word1[l]
                l += 1
            if r < len(word2):
                result += word2[r]
                r += 1
        return result
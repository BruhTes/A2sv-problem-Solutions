# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        # horisontal scaling principle
        for i in range(1, len(strs)):
            while(strs[i].find(prefix) != 0):
                prefix = prefix[0: len(prefix) - 1]

                if prefix == "":
                    return ""
        return prefix
            
# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        s = Counter(s)
        t = Counter(t)

        if len(s) > len(t):
            for key in s:
                if s[key] != t[key]:
                    return False
        else:
            for key in t:
                if t[key] != s[key]:
                    return False
        return True         
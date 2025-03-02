# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        exist = set()
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in exist:
                dic[s[i]] = t[i]
                exist.add(t[i])
            elif s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                return False
        return True
# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
            
        n = len(s1)
        s1 = Counter(s1)
            
        for i in range(len(s2) - 1):
            subStr = Counter(s2[i : i + n])
            if subStr == s1:
                return True
        return False
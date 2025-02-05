# Problem: Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swaps = 0
        count1 = Counter(s1)
        count2 = Counter(s2)
        
        if count1 != count2:
            return False
            
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps += 1
        
        return swaps <= 2
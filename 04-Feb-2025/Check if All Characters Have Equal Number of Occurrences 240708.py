# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        letter = s[0]
        s = Counter(s)
        occ = s[letter]
        
        print(occ)
        for key in s:
            if s[key] != occ:
                return False
        return True
# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        allowed_ = set(allowed)

        for word in words:
            if all(char in allowed_ for char in word):
                count += 1
        
        return count

# Time = O(n + n * k) = O(nk)
# Space = O(n)
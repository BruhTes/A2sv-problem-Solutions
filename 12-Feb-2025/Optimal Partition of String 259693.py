# Problem: Optimal Partition of String - https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        unique = set()
        left = 0
        for right in range(len(s)):
            unique.add(s[right])
            if len(unique) != right - left + 1:
                count += 1
                unique = set(s[right],)
                print(unique)
                left = right
        
        return count + 1

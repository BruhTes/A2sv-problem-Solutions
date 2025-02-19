# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        onesCount = s.count('1')
        n = len(s)
        score = 0
        runningZero = 0
        runningOnes = 0

        for i in range(n - 1): 
            if s[i] == '0':
                runningZero += 1
            else:
                runningOnes += 1
            score = max(score, runningZero + onesCount - runningOnes)
        
        return score
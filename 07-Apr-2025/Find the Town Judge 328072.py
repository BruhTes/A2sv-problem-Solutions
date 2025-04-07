# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0 for i in range(n)]
        trusted = [0 for i in range(n)]

        for x in trust:
            a, b = x
            trusts[a - 1] += 1
            trusted[b - 1] += 1
        
        for i in range(n):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i + 1
        return -1
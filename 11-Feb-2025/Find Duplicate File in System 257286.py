# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        con =defaultdict(list)
        for i in paths:
            r = i.split(' ')
            
            for j in range(1,len(r)):
                br = r[j].split('(')
                con[br[-1]].append(r[0]+"/"+br[0]) 

        ans = []
        for val in con.values():
            if len(val) > 1:
                ans.append(val)
        return ans
# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m = {}
        for i, s in enumerate(list1):
            m[s] = i
        
        smallest = float('inf')
        res = []
        for i, s in enumerate(list2):
            if s in m and (m[s] + i) < smallest:
                res = [s]
                smallest = i+m[s]
            elif s in m and (m[s] + i) == smallest:
                res.append(s)
        
        return res
            
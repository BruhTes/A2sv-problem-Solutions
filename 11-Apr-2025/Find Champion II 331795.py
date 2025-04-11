# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # graph = defaultdict(list)
        # for edge in edges:
        #     a, b = edge
        #     graph[a].append(b)
        
        # print(graph)
        result = [0 for i in range(n)]
        for edge in edges:
            a, b = edge
            result[b] += 1
        
        res = []
        for i, r in enumerate(result):
            if r == 0:
                res.append(i)
        
        if len(res) != 1:
            return -1
        else:
            return res[0]
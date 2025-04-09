# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # form the adjacency list of the graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        # label the colors
        white = 1
        gray = 2
        black = 3

        # assign white for each course
        colors = {k : white for k in range(numCourses)}
        cycle_detected = False

        def dfs(node):
            nonlocal cycle_detected

            if cycle_detected:
                return
            
            colors[node] = gray

            for neighbour in graph[node]:
                if colors[neighbour] == white:
                    dfs(neighbour)
                elif colors[neighbour] == gray:
                    cycle_detected = True
            
            colors[node] = black
        
        for i in range(numCourses):
            if colors[i] == white:
                dfs(i)
                if cycle_detected:
                    return False
        
        return True
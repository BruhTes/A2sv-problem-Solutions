# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def find_max(grid, x, y):
            max_element = 0
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    max_element = max(max_element, grid[i][j])
            
            return max_element
        
        n = len(grid)
        
        max_local = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                max_local[i][j] = find_max(grid, i, j)
        
        return max_local

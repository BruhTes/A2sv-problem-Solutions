# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def inbound(self, r, c, m, n):
        return 0 <= r <= m - 1 and 0 <= c <= n - 1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        fresh = 0
        m = len(grid)
        n = len(grid[0])

        # count freshes and rooted ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if fresh == 0:
            return 0
        
        # BFS traversal
        minute = 0
        while queue and fresh > 0:
            queue_len = len(queue)

            for i in range(queue_len):
                a, b = queue.popleft()
                visited.add((a, b))
                for s, d in directions:
                    r, c = a + s, b + d
                    if self.inbound(r, c, m, n) and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] += 1
                        queue.append((r, c))
            minute += 1
            
        return minute if fresh <= 0 else -1
# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        diagonal_traverse = []

        direction = 1 # 1 for upright and -1 for downleft
        i = 0
        j = 0

        for _ in range(rows * cols):
            diagonal_traverse.append(mat[i][j])

            if direction == 1:
                if j == cols - 1:
                    direction = -1
                    i += 1
                elif i == 0:
                    direction = -1
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == rows - 1:
                    direction = 1
                    j += 1
                elif j == 0:
                    direction = 1
                    i += 1
                else:
                    i += 1
                    j -= 1
        return diagonal_traverse

# Time = O(n * m)
# Space = O(n * m)
# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        def rotate90(mat):
            rows = len(mat)
            cols = len(mat[0])
            
            rotated_mat = [[0]*cols for row in range(rows)]

            for i in range(rows):
                for j in range(cols):
                    rotated_mat[j][rows - i - 1] = mat[i][j]
            return rotated_mat

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate90(mat)
        return False


# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []

        for col in range(len(matrix[0])):
            curr_row = []
            for row in range(len(matrix)):
                curr_row.append(matrix[row][col])
            
            transpose.append(curr_row)
        
        return transpose
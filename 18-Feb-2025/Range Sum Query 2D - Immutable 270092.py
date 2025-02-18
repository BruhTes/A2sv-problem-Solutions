# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        
        self.prefixSum = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                self.prefixSum[i][j] = matrix[i][j] + (self.prefixSum[i - 1][j] if i > 0 else 0) + (self.prefixSum[i][j - 1] if j > 0 else 0) - (self.prefixSum[i - 1][j - 1] if i > 0 and j > 0 else 0)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.prefixSum[row2][col2]

        if row1 > 0:
            total -= self.prefixSum[row1 - 1][col2]
        if col1 > 0:
            total -= self.prefixSum[row2][col1 - 1]
        if col1 > 0 and row1 > 0:
            total += self.prefixSum[row1 - 1][col1 - 1]
        
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
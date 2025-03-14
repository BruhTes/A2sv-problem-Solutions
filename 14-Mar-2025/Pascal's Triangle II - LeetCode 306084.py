# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 1:
            return [1, 1]
        if rowIndex == 0:
            return [1]

        result = [1]
        previous = self.getRow(rowIndex - 1)

        for i in range(len(previous) - 1):
            result.append(previous[i] + previous[i + 1])
        result.append(1)
        
        return result
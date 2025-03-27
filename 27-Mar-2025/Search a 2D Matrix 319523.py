# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # FInding the row where target might exist
        low, high = 0, len(matrix) - 1
        row = -1
        while low <= high:
            mid = low + (high - low) // 2

            if matrix[mid][0] <= target:
                low = mid + 1
                row = mid
            else:
                high = mid - 1
        
        if row == -1:
            row = len(matrix) - 1

        # binary search on that row
        low, high = 0, len(matrix[row]) - 1
        while high >= low:
            mid = low + (high - low) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
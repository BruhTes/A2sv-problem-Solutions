# Problem: Final Value of Variable After Performing Operations - https://leetcode.com/problems/final-value-of-variable-after-performing-operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        plus = 0
        minus = 0
        for i in range(len(operations)):
            if "+" in operations[i]:
                plus += 1
            else:
                minus += 1
        return plus - minus
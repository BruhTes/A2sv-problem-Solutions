# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        result = []
        if num % 3 != 0:
            return result
        else:
            result.append((num // 3) - 1)
            result.append((num // 3))
            result.append((num // 3) + 1)
            return result

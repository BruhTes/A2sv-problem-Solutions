# Problem: Car Pooling - https://leetcode.com/problems/car-pooling/description/

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxLen = 10000
        indexUsage = [0] * (maxLen + 1)
    
        for numP, start, end in trips:
            indexUsage[start] += numP
            if end < len(indexUsage):
                indexUsage[end] -= numP
        
        for i in range(len(indexUsage)):
            indexUsage[i] += indexUsage[i - 1] if i - 1 >= 0 else 0
            if indexUsage[i] > capacity:
                return False
        print(indexUsage)
        return True

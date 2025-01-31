# Problem: Water Bottles - https://leetcode.com/problems/water-bottles/description

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sum = numBottles
        
        while(numBottles >= numExchange):
            sum += numBottles//numExchange
            
            numBottles = numBottles % numExchange + numBottles // numExchange
        
        return sum
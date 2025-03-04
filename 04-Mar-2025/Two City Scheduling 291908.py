# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first = [costs[i][0] for i in range(len(costs))]
        diff = [costs[i][0] - costs[i][1] for i in range(len(costs))]

        print(sorted(diff, reverse = True))
        return sum(first) - sum(sorted(diff, reverse = True)[0 : len(costs) // 2])
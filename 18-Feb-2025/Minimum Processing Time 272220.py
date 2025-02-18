# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse = True)
        processorTime.sort()
        i = 0
        j = 0

        time = 0
        while i < len(tasks):
            time = max(time, processorTime[j] + tasks[i])
            j += 1
            i += 4
        
        return time
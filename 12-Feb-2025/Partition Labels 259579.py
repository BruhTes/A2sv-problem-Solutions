# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = {char: i for i, char in enumerate(s)}
        
        start = 0
        end = 0
        partitions = []

        for i in range(len(s)):
            end = max(end, last_occurence[s[i]])

            if i == end:
                partitions.append(end - start + 1)
                start = end + 1
        
        return partitions
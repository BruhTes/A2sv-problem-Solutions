# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        for i in range(1, len(score)):
            j = i

            while j > 0 and score[j][k] > score[j-1][k]:
                score[j], score[j-1] = score[j-1], score[j]
                j -= 1

        return score
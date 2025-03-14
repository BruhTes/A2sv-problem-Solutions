# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        people = deque(range(1, n + 1))

        while len(people) > 1:
            for i in range(k - 1):
                a = people.popleft()
                people.append(a)
            people.popleft()
        
        return people[0]
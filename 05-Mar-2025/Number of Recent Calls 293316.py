# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.queue = []
        self.index = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[self.index] < t - 3000:
            self.index += 1
        return len(self.queue) - self.index


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
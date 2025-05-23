# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.val = value
        self.k = k
        self.count = 0

    def consec(self, num: int) -> bool:
        if len(self.queue) >= self.k:
            curr = self.queue.popleft()
            if curr == self.val:
                self.count -= 1
        self.queue.append(num)
        if num == self.val:
            self.count += 1
        return self.k == self.count
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        
        if num != self.value:
            while self.queue:
                self.queue.popleft()
        
        return len(self.queue) >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
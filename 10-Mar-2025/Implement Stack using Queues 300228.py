# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

        # reverse it to move the current element to the front
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        if self.stack:
            return self.stack.popleft()
        return -1

    def top(self) -> int:
        if self.stack:
            return self.stack[0]
        return -1

    def empty(self) -> bool:
        return not self.stack


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
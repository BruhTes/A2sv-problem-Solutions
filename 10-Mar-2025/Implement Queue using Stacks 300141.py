# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.stack = []
        self.pointer = 0

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.pointer < len(self.stack):
            self.pointer += 1
            return self.stack[self.pointer - 1]
        return -1

    def peek(self) -> int:
        if self.pointer < len(self.stack):
            return self.stack[self.pointer]
        return -1


    def empty(self) -> bool:
        return self.pointer >= len(self.stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
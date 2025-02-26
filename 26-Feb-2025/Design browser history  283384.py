# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
    
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.current
        self.dummy_tail.prev = self.current

        self.current.prev = self.dummy_head
        self.current.next = self.dummy_tail

    def visit(self, url: str) -> None:
        newNode = Node(url, self.current, self.dummy_tail)
        newNode.prev = self.current
        newNode.next = self.dummy_tail
        
        self.current.next = newNode
        self.dummy_tail.prev = newNode
        self.current = newNode

    def back(self, steps: int) -> str:
        while self.current.prev != self.dummy_head and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.value

    def forward(self, steps: int) -> str:
        while self.current.next != self.dummy_tail and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.value



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
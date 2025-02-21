# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # create a hashmap for the cache
        self.capacity = capacity
        self.cache = {}
        # create a dummy node on both ends for ease
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertAtFront(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode
        

    def remove(self, newNode):
        prevNode = newNode.prev
        nextNode = newNode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            # move the node to head (remove and insert)
            current = self.cache[key]
            self.remove(current)
            self.insertAtFront(current)
            return current.value
        # else return -1
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.insertAtFront(newNode)
        self.cache[key] = newNode
        
        if len(self.cache) > self.capacity:
            remove_ = self.tail.prev
            self.remove(remove_)
            del self.cache[remove_.key]


        # if len(self.cache) < self.capacity:
        #     # add it to the head
        #     if key in self.cache:
        #         self.remove(self.cache[key])
            
        #     newNode = Node(key, value)
        #     self.insertAtFront(newNode)
        #     self.cache[key] = newNode
        # else:
        #     newNode = Node(key, value)
        #     if key in self.cache:
        #         self.remove(self.cache[key])
        #         self.insertAtFront(newNode)
        #         self.cache[key] = newNode
        #     else:
        #         # remove the tail node and add newnode to the front
        #         self.remove(self.tail.prev)
        #         seff.insertAtFront(newNode)

# I need "add to front" function 
# and a remove funciton to remove the least priority element

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
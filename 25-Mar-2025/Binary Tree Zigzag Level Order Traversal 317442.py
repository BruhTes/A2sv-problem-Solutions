# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def helper(level, queue):
            if not queue:
                return
            
            queueLen = len(queue)
            current = []
            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    current.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if current:
                if level % 2 == 1:
                    self.result.append(current[::-1])
                else:
                    self.result.append(current)
            
            helper(level + 1, queue)
        
        queue = deque()
        queue.append(root)
        helper(0, queue)
        return self.result
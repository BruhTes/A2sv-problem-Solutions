# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(queue, level):
            if not queue:
                return
            queueLen = len(queue)

            if level % 2 == 0:
                for i in range(queueLen):
                    node = queue.popleft()
                    if node:
                        queue.append(node.left)
                        queue.append(node.right)
                bfs(queue, level + 1)
            else:
                new = deque()
                for node in queue:
                    if node:
                        new.append(node.left)
                        new.append(node.right)
                    
                while queue:
                    left = queue.popleft()
                    right = queue.pop()
                    if left and right:
                        left.val, right.val = right.val, left.val
                
                bfs(new, level + 1)
            
        queue = deque()
        queue.append(root)
        bfs(queue, 0)
        return root
# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:        
        if not root:
            return self.result
        
        def bfs(queue):
            if not queue:
                return

            queueLen = len(queue)
            max_ = float('-inf')

            for i in range(queueLen):
                node = queue.popleft()
                if node:
                    max_ = max(max_, node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            if max_ != float('-inf'):
                self.result.append(max_)
            
            bfs(queue)
        
        queue = deque()
        queue.append(root)
        bfs(queue)
        return self.result
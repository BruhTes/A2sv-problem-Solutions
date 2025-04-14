# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(root)
        val = root.val

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    if node.val != val:
                        return False
                    queue.append(node.left)
                    queue.append(node.right)
        
        return True
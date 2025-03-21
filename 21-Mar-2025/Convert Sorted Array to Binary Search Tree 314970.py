# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def bst(left, right):
            if left > right:
                return None
            
            middle = left + (right - left) // 2

            leftNode = bst(left, middle - 1)

            rightNode = bst(middle + 1, right)

            return TreeNode(nums[middle], leftNode, rightNode)
        
        return bst(0, len(nums) - 1)
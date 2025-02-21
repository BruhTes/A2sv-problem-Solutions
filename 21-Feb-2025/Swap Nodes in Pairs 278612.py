# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.val, second.val = second.val, first.val

            prev = prev.next.next
        
        return dummy.next
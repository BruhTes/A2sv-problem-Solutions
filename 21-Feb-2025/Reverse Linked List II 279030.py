# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        start = dummy
        for i in range(left - 1):
            start = start.next
        
        # reverse the aimed place
        next = None
        prev = None
        curr = start.next
        for i in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        start.next.next = curr
        start.next = prev
        
        return dummy.next
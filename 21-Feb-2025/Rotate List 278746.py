# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        curr = head
        newEnd = head
        n = 1
        while curr.next:
            n += 1
            curr = curr.next
        k = k % n

        if n == k or k == 0:
            return head
        for i in range(n - k - 1):
            newEnd = newEnd.next
            
        newHead = newEnd.next
        newEnd.next = None
        curr.next = head
        return newHead
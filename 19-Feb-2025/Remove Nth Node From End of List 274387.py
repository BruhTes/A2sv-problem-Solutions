# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        prev, curr = None, head
        for i in range(count):
            if i == count - n:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
                break
            else:
                prev, curr = curr, curr.next
        
        return head
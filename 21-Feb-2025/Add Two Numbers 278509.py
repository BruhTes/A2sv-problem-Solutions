# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        c = 0

        while l1  or l2 or c != 0:
            curr = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            c = curr // 10
            
            newNode = ListNode(curr % 10)
            current.next = newNode
            current = newNode

            # update l1 and l2
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
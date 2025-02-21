# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = head
        placeholder = dummy

        while current:
            if current.next and current.val == current.next.val:
                while current.next and current.val == current.next.val:
                    current = current.next
                placeholder.next = current.next
            else:
                placeholder = placeholder.next
            current = current.next
        return dummy.next
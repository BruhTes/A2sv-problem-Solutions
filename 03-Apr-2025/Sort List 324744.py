# Problem: Sort List - https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow = head
        # set fast to head.next to set the left.next none afterwards
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left_head = head
        right_head = self.getMid(head)

        # set the end of the left
        temp = right_head.next
        right_head.next = None
        right_head = temp

        # call right and left recursively
        left = self.sortList(left_head)
        right = self.sortList(right_head)
        return self.merge(left, right)
# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                current.next = newNode
                current = newNode
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                current.next = newNode
                current = newNode
                list2 = list2.next
            
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next
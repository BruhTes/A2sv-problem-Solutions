# Problem: Reverse Linked List - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        placeholder = head
        seeker = head.next
        
        while seeker:
            curr =  seeker.next
            seeker.next = placeholder
            placeholder = seeker
            seeker = curr# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        placeholder = None
        seeker = head
        
        while seeker:
            curr =  seeker.next
            seeker.next = placeholder
            placeholder = seeker
            seeker = curr
        
        return placeholder
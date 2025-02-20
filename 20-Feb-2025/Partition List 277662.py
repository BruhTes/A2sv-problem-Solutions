# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        lowers = None
        highers = None
        
        # pL - pointer for tail of lowers and pH - pointer for tail of highers
        current = head
        pL = None
        pH = None
        while current:
            if current.val < x:
                if not lowers:
                    lowers = current
                    pL = lowers
                else:
                    pL.next = current
                    pL = current
            else:
                if not highers:
                    highers = current
                    pH = highers
                else:
                    pH.next = current
                    pH = current
            
            current = current.next
        
        if pL:
            pL.next = highers
            if pH:
                pH.next = None
            return lowers
    
        return highers

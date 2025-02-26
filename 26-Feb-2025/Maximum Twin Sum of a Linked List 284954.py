# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        max_ = 0
        while prev:
            max_ = max(max_, prev.val + head.val)
            head, prev = head.next, prev.next
        print(max_)
        return max_
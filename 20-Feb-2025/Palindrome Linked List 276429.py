# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the linked list
        placeholder = None
        seeker = slow
        while seeker:
            curr = seeker.next
            seeker.next = placeholder
            placeholder = seeker
            seeker = curr

        left = head
        right = placeholder
        while right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        
        return True
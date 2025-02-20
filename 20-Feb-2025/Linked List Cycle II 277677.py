# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def isCycle(tortoise, rabbit):
            while rabbit and rabbit.next:
                tortoise = tortoise.next
                rabbit = rabbit.next.next

                if tortoise == rabbit:
                    return tortoise
            return None
        
        tortoise = head
        rabbit = head
        meeting_point = isCycle(tortoise, rabbit)
        if not meeting_point:
            return None
        
        tortoise = head
        while tortoise != meeting_point:
            tortoise = tortoise.next
            meeting_point = meeting_point.next
        
        return tortoise
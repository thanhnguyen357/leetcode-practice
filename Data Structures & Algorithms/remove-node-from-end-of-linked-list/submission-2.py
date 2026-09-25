# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for i in range(n):
            end = end.next
        
        dummy = ListNode(None, head)
        prev = dummy
        while end:
            prev = prev.next
            end = end.next
        
        prev.next = prev.next.next

        return dummy.next
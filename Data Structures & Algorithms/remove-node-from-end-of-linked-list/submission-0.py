# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None and n != 0:
            return None  
        
        last = head
        count_last = 1
        while last.next:
            last = last.next
            count_last += 1
        
        count = 1
        prev = head
        temp = None
        while prev:
            if count == count_last - (n-1):
                temp.next = prev.next
                return head
            
            temp = prev
            prev = prev.next
            count += 1
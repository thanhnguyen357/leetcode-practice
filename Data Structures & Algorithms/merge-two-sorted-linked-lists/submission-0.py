# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        l1 = list1
        l2 = list2

        current = dummy
        while (l1 != None and l2 != None):
            if (l2.val <= l1.val):
                current.next = l2
                current = current.next
                l2 = l2.next
            else:
                current.next = l1
                current = current.next
                l1 = l1.next
        if (l1 is None):
            current.next = l2
        else:
            current.next = l1
        return dummy.next

        
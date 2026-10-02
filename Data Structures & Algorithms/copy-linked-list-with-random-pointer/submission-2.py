"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        result = {}

        temp = head    
        while temp:
            result[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            result[temp].next = result.get(temp.next)
            result[temp].random = result.get(temp.random)

            temp = temp.next
        
        return result[head]
        
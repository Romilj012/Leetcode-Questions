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
        copyOldNodes = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            copyOldNodes[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = copyOldNodes[curr]
            copy.next = copyOldNodes[curr.next]
            copy.random = copyOldNodes[curr.random]
            curr = curr.next 
        return copyOldNodes[head]  
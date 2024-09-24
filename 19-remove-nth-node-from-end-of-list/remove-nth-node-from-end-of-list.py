# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both fast and slow pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node
        slow.next = slow.next.next
        
        # Return the modified list
        return dummy.next


        
        
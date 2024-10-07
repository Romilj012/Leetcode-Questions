# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = ListNode()
        p = finalList
        for i in lists:
            head = i
            while head:
                p.next = head
                head = head.next
                p = p.next
        print(finalList.next)
        finalListsort = ListNode()
        q = finalListsort
        # while finalList.next:
        #     if finalList.next.val < finalList.next.next.val:
        #         q.next = finalList.next
        #         finalList.next = finalList.next.next
        #         q = q.next
        #         print(finalListsort.next)
        #     else:
        #         q.next = finalList.next.next
        #         finalList.next.next = finalList.next
        #         q = q.next
        #         print(finalListsort.next)
        #     finalList.next = finalList.next.next
        # return finalListsort.next 
        if finalList.next is None or finalList.next.next is None:
            return finalList.next
        swapped = True
        while swapped:
            swapped = False
            current = finalList.next
            while current.next is not None:
                if current.val  > current.next.val:
                    # Swap the nodes
                    current.val, current.next.val = current.next.val, current.val
                    swapped = True
                current = current.next
        return finalList.next
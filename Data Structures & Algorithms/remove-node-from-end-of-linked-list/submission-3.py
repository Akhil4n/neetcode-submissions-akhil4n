# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz = 0
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        target = sz - n + 1
        prev = None
        curr = head
        cz = 0
        if target == 1:
            return head.next
        while curr:
            cz += 1
            if cz == target:
                nx = curr.next
                prev.next = nx
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head

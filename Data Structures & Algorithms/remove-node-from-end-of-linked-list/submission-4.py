# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        for i in range(n):
            fast = fast.next
        dummy = ListNode(0, head)
        curr = dummy
        while fast:
            fast = fast.next
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
        
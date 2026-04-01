# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr:
            end = curr
            while end.next and end.next.next:
                end = end.next
            temp1 = end.next
            end.next = None
            temp2 = curr.next
            curr.next = temp1
            if temp1:
                temp1.next = temp2
            curr = temp2
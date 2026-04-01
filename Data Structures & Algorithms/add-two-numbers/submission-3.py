# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryIn = 0
        dummy = ListNode()
        head = dummy
        while l1 and l2:
            curVal = l1.val + l2.val
            if carryIn == 1:
                curVal += 1
            if curVal >= 10:
                curVal -= 10
                carryIn = 1
            else:
                carryIn = 0
            head.next = ListNode(curVal)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        while l1:
                curVal = l1.val
                if carryIn == 1:
                    curVal += 1
                if curVal >= 10:
                    curVal -= 10
                    carryIn = 1
                else:
                    carryIn = 0
                head.next = ListNode(curVal)
                head = head.next
                l1 = l1.next
        while l2:
                curVal = l2.val
                if carryIn == 1:
                    curVal += 1
                if curVal >= 10:
                    curVal -= 10
                    carryIn = 1
                else:
                    carryIn = 0
                head.next = ListNode(curVal)
                head = head.next
                l2 = l2.next
        if carryIn == 1:
            head.next = ListNode(1)
        return dummy.next

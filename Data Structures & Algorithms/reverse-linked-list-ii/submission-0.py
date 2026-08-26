class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pre = None
        post = None

        prev = None
        leftNode = None
        rightNode = None

        curr = head
        position = 1
        while curr:
            if position == left - 1:
                pre = curr
            if position == right + 1:
                post = curr
            if left <= position and right >= position:
                if position == left:
                    leftNode = curr
                if position == right:
                    rightNode = curr
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            else:
                prev = curr
                curr = curr.next
            position += 1
        
        if leftNode:
            leftNode.next = post
        if pre:
            pre.next = rightNode
        if head == leftNode:
            head = rightNode
        return head
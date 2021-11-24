'''
使用python特性使代码简洁
'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val
            carry, val = divmod(val, 10)
           # curr, curr.next = ListNode(val, None), curr
            curr.next = curr = ListNode(val)
        return head.next

'''
leetcode 执行快速有时是因为测试用例比较适用于算法，或服务器更快了
要考虑代码本身的计算量
'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l1 if l1 else l2

        f = 0
        h = ListNode()
        p = h
        while l1 and l2:
            s = l1.val + l2.val + f
            f = s // 10
            p.next = ListNode(s % 10)
            p = p.next
            l1, l2 = l1.next, l2.next

        l1 = l1 if l1 else l2
        while l1:
            s = l1.val + f
            f = s // 10
            p.next = ListNode(s % 10)
            p, l1 = p.next, l1.next
        if f:
            p.next = ListNode(f)
        return h.next

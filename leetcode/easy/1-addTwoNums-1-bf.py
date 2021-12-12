'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

事例：
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
'''


'''
这种方法可行，但复杂 （暴力算法，自己思考）
'''


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        c = 0
        while l1 != None:
            num1 = num1 + l1.val * 10 ** c
            l1 = l1.next
            c += 1
        c = 0
        while l2 != None:
            num2 = num2 + l2.val * 10 ** c
            l2 = l2.next
            c += 1
        num = num1 + num2
        print(num1, ' + ', num2, ' = ', num)
        if num == 0:
            return ListNode(0, None)
        front = ListNode()
        cur = front
        while num != 0:
            n = num % 10
            num //= 10
            tmp = ListNode(n, None)
            cur.next = tmp
            cur = tmp
        return front.next


if __name__ == '__main__':
    num1 = [2, 4, 9]
    num2 = [5, 6, 4, 9]
    l1 = ListNode()
    cur = l1
    for i in range(len(num1)):
        tmp = ListNode(num1[i], None)
        cur.next = tmp
        cur = tmp
    l1 = l1.next
    l2 = ListNode()
    cur = l2
    for i in range(len(num2)):
        tmp = ListNode(num2[i], None)
        cur.next = tmp
        cur = tmp
    l2 = l2.next
    solution = Solution()
    list_r = solution.addTwoNumbers(l1, l2)
    result = [0] * 5
    for i in range(5):
        result[i] = list_r.val
        list_r = list_r.next
    print(num1, " + ", num2, " = ", result)
    print(l1.val, '   ', l2.val)

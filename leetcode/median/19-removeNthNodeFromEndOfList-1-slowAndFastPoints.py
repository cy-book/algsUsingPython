'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

思路： 快慢指针
'''

# date: 2021-12-12
# author: cy-book

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    cur = head
    frontOfN = head
    for i in range(n):
        cur = cur.next
    if not cur:
        return frontOfN.next
    while cur.next:
        cur = cur.next
        frontOfN = frontOfN.next
    frontOfN.next = frontOfN.next.next
    return head

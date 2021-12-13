'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    head = ListNode()
    cur = head
    while list1 and list2:
        if(list1.val < list2.val):
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    while list1:
        cur.next = list1
        cur = cur.next
        list1 = list1.next
    while list2:
        cur.next = list2
        cur = cur.next
        list2 = list2.next
    return head.next

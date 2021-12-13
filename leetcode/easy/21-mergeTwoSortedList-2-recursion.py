# 参考: https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
# date: 2021-12-13
# author: cy-book

from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    if list1 and list2:
         if list1.val < list2.val:
             head = list1
             head.next = mergeTwoLists(list1.next, list2)
         else:
             head = list2
             head.next = mergeTwoLists(list1, list2.next)
         return head
     elif list1:
         return list1
     elif list2:
         return list2
     return None
    '''
    if not list1:
        return list2
    elif not list2:
        return list1
    elif list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


def createList(nums: List[int]) -> ListNode:
    prehead = ListNode()
    cur = prehead
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return prehead.next


def nodeToList(head: ListNode) -> List[int]:
    result = list()
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == '__main__':
    inputList = [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])]
    for list1, list2, ans in inputList:
        l1 = createList(list1)
        l2 = createList(list2)
        outputVal = nodeToList(mergeTwoLists(l1, l2))
        print(list1, list2, ans)
        print(outputVal)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution251116:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        result = None
        tail = None
        while list1 and list2:
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            if not tail:
                result = ListNode(val)
                tail = result
            else:
                tail.next = ListNode(val)
                tail = tail.next

        if tail and list1:
            tail.next = list1
        elif tail and list2:
            tail.next = list2

        return result

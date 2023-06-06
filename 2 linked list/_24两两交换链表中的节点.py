# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head

        # while cur.next is not None and cur.next.next.next is not None:
        # 这里只要cur.next.next不为空，则cur.next.next存在next，只是next为None而已，所以写到cur.next.next即可
        while cur.next is not None and cur.next.next is not None:
            tmp1 = cur.next
            tmp2 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = tmp1
            cur.next.next.next = tmp2
            cur = cur.next.next

        return dummy_head.next
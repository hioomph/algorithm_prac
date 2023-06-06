# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        # while cur.next is not None: 这里的cur不是dummy_head而是head，所以直接对cur进行判断即可
        while cur is not None:
            tmp = cur.next
            # pre.next = cur.next.next
            # cur.next.next = cur
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

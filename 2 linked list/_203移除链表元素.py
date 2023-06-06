# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur = dummy_head
        while cur.next is not None:
            # 这里如果用cur.val === val来判断相等时，想要删除就得要知道cur前面的节点；
            # 判断是否等于val是cur.next.val == = val，所以while循环条件是cur.next, 而不是cur
            if cur.next.val == val:
                # cur = cur.next 移出链表元素的关键步骤，但写错了
                cur.next = cur.next.next
            # cur = cur.next 这里如果直接放在while循环中的话，则cur可能会直接跳过val值所在的节点
            else:
                cur = cur.next
        # return head 这里的head有可能已经被删除了，所以应该返回dummy_head.next，确保返回有效
        return dummy_head.next
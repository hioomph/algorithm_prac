# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA, curB = headA, headB
        countA, countB = 0, 0
        while curA:
            curA = curA.next
            countA += 1
        while curB:
            curB = curB.next
            countB += 1

        # 上述遍历是为了求长度，因此一定不要忘记把curA，curB重新指向表头！！！
        curA, curB = headA, headB

        # 保证A的长度大于等于B，若小于则进行交换
        if countA < countB:
            tmp = curB
            curB = curA
            curA = tmp
        diff = abs(countB-countA)

        # 判断是否相交
        # 首先将curA后移diff位
        while diff > 0:
            curA = curA.next
            diff -= 1
        # 判断相交点
        while curA and curB:
            # if curA.val == curB.val:
            if curA == curB:  # 不是val相等，是指针相等！
                return curA
            curA = curA.next
            curB = curB.next
        return None


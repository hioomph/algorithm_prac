class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        # if index < 0 or index > self.size:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        new_head = Node(val=val)
        new_head.next = self.head.next
        self.head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return

        node = Node(val)
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        node.next = pre.next
        pre.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

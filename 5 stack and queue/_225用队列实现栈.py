class MyStack:

    def __init__(self):
        from collections import deque
        self.my_queue = deque()

    def push(self, x: int) -> None:
        self.my_queue.append(x)

    def pop(self) -> int:
        return self.my_queue.pop()

    def top(self) -> int:
        tmp = self.pop()
        self.push(tmp)
        return tmp

    def empty(self) -> bool:
        if not self.my_queue:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_2,param_3,param_4)
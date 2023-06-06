class MyQueue:

    def __init__(self):
        # 定义两个栈，一个用于in元素，一个用于out元素
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # 将x压入stack_in中
        self.stack_in.append(x)

    def pop(self) -> int:
        # 首先看stack_in中是否有元素，有的话全部导入到stack_out中
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        tmp = self.pop()
        self.stack_out.append(tmp)
        return tmp

    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        return False

from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def partition(self, s: str) -> List[List[str]]:
        self.result.clear()
        self.path.clear()
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s: str, start_index: int):
        # Base Case
        if start_index >= len(s):
            self.result.append(self.path)
            return

        # 单层搜索
        for i in range(start_index, len(s)):
            # 判断是否回文串
            temp = s[start_index:i+1]
            if temp == temp[::-1]:
                self.path.append(temp)
                self.backtracking(s, i+1)
                self.path.pop()
            else:
                continue
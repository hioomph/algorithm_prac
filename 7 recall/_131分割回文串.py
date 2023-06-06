from typing import List


class Solution:
    def __init__(self):
        self.result = []  # 存放结果集
        self.path = []  # 存放切割后回文的子串

    def partition(self, s: str) -> List[List[str]]:
        self.path.clear()
        self.result.clear()
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s: str, startIndex: int):
        # Base case
        if startIndex >= len(s):
            self.result.append(self.path[:])
            return

        # 单层搜索
        for i in range(startIndex, len(s)):
            temp = s[startIndex:i + 1]
            if temp == temp[::-1]:  # temp为回文串
                self.path.append(temp)
            else:
                continue
            self.backtracking(s, i+1)
            self.path.pop()

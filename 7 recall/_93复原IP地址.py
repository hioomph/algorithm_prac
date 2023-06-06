from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result.clear()
        if len(s) > 12:
            return []
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s: str, startIndex: int, pointNum: int):
        '''
        :param s:
        :param startIndex: 搜索的起始位置
        :param pointNum:   添加逗点的数量
        '''
        # Base case
        if pointNum == 3:
            if self.isValid(s, startIndex, len(s)-1):
                self.result.append(s)
            return

        # 单层搜索
        for i in range(startIndex, len(s)):
            # [start_index, i]就是被截取的子串
            if self.isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]
                self.backtracking(s, i+2, pointNum+1)
                s = s[:i+1] + s[i+2:]  # 回溯
            else:
                # 若当前被截取的子串大于255或者大于三位数，直接结束本层循环
                break

    def isValid(self, s: str, start: int, end: int):
        if start > end:
            return False
        # 若数字是 0 开头，不合法
        if s[start] == '0' and start != end:
            return False
        if not 0 <= int(s[start:end + 1]) <= 255:
            return False
        return True

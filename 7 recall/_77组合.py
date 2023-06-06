from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 定义两个全局变量
        result = []  # 存放符合条件的结果的集合
        path = []  # 存放符合条件的结果

        def backtracking(n: int, k: int, startindex: int):
            # 终止条件
            if len(path) == k:
                # result.append(path)
                result.append(path[:])
                return

            # 单层搜索
            # for循环每次从startIndex开始遍历，然后用path保存取到的节点i
            # 剪枝操作
            endindex = n - (k - len(path)) + 1
            for i in range(startindex, endindex+1):
                path.append(i)
                backtracking(n, k, i+1)
                path.pop()  # 回溯

        backtracking(n, k, 1)
        return result




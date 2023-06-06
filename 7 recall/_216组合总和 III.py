from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        sum = 0

        def backtracking(k, n, starindex):
            nonlocal sum

            if sum > n:  # 剪枝
                return
            if len(path) == k:
                if sum == n:
                    result.append(path[:])
                return

            # for i in range(starindex, 10):
            for i in range(starindex, 10 - (k - len(path)) + 1):
                path.append(i)
                sum += i
                backtracking(k, n, i+1)
                path.pop()
                sum -= i

        backtracking(k, n, 1)
        return result

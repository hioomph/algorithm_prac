from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        sum = 0

        def backtracking(candidates, target, starindex):
            nonlocal path
            nonlocal sum

            if sum == target:
                result.append(path[:])
                return
            if sum > target:
                return

            for i in range(starindex, len(candidates)):
                sum += candidates[i]
                path.append(candidates[i])
                # backtracking(candidates, target, starindex)
                backtracking(candidates, target, i)
                sum -= candidates[i]
                path.pop()

        path.clear()
        result.clear()
        backtracking(candidates, target, 0)
        return result

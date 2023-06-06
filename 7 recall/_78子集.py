from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums: List[int], startIndex: int):
        self.result.append(self.path[:])  # 放在终止条件的上面，防止漏掉自己
        # Base case
        if startIndex >= len(nums):
            return

        # 单层递归
        for i in range(startIndex, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()


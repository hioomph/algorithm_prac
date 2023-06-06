from typing import List

# 本题和题目 40 解法一致
class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums: List[int], startIndex: int):
        self.result.append(self.path[:])  # 放在终止条件的上面，防止漏掉自己
        # Base case
        if startIndex >= len(nums):
            return

        # 单层递归
        for i in range(startIndex, len(nums)):
            if i > 0 and self.used[i-1] == False and nums[i] == nums[i-1]:
                continue

            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums, i+1)
            self.path.pop()
            self.used[i] = False


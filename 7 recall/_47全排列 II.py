from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.used = [False] * len(nums)
        nums.sort()
        self.backtracking(nums)
        return self.result

    def backtracking(self, nums: List[int]):
        # Base case
        if len(self.path) >= len(nums):
            self.result.append(self.path[:])
            return

        # 单层递归
        for i in range(len(nums)):
            if self.used[i]:
                continue
            if i>0 and self.used[i-1] == False and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            self.path.pop()
            self.used[i] = False
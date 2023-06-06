from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.path = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.result.clear()
        self.path.clear()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums: List[int], startIndex: int):
        if len(self.path) >= 2:
            self.result.append(self.path[:])
        if startIndex >= len(nums):
            return

        # 深度遍历中每一层都会有一个全新的usage_list用于记录本层元素是否重复使用
        usage_list = set()
        for i in range(startIndex, len(nums)):
            if (self.path and nums[i] < self.path[-1]) or (nums[i] in usage_list):
                continue

            usage_list.add(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()



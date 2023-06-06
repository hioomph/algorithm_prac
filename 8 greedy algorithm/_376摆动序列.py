from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        preDiff, curDiff = 0, 0
        result = 1  # 初始化为1
        for i in range(1, len(nums)):
            curDiff = nums[i-1] - nums[i]
            if (preDiff <= 0 and curDiff > 0) or (preDiff >= 0 and curDiff < 0):
                result += 1
                preDiff = curDiff
        return result

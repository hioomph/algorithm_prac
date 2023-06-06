from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 这道题如果采用贪心的思想，贪心的点在于”当两个连续数字的和为负数时，即舍弃当前这组数“
        res = -float('inf')
        tmp = 0

        for i in range(len(nums)):
            tmp += nums[i]
            if tmp >= res:
                res = tmp
            if tmp <= 0:
                tmp = 0

        return res





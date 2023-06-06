from typing import List

"""
在本题中实现滑动窗口，主要确定如下三点：
    窗口内是什么？
    如何移动窗口的起始位置？
    如何移动窗口的结束位置？

窗口就是 满足其和 ≥ s 的长度最小的 连续 子数组。
窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0  # 窗口起始位置
        j = 0  # 窗口终止位置
        res = float("inf")   # 定义一个无限大的数
        sum = 0  # 存放窗口内容
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                res = min(res, j-i+1)
                sum -= nums[i]
                i += 1
        return 0 if res == float("inf") else res
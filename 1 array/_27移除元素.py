"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并原地修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

思路：
    暴力解法 & 双指针法
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = low = 0
        while fast < len(nums):
            # @1
            if nums[fast] == val:
                fast += 1
            # 这里两个if是并列关系，假设第一个if成立，fast值加1更新后，则会带着这个fast值继续进行第2个if判断
            # 因此应该写if-elif
            # if nums[fast] != val:
            elif nums[fast] != val:
                nums[low] = nums[fast]
                fast += 1
                low += 1

            # @2
            """
            if nums[fast] != val:
                nums[low] = nums[fast]
                low += 1
            fast += 1
            """
        return low

    res = removeElement(object, [1,2,3,4,2],2)
    print(res)
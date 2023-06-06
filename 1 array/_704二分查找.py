# 数组下标都是从0开始的
# 数组内存空间的地址是连续的
# 数组的元素是不能删的，只能覆盖

from typing import List

"""
思路：
    题目中的“有序数组（升序）”和“无重复元素”提示本题可以采用二分查找。
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] <= target <= nums[right]:
                # mid = (left+right)//2
                mid = left + ((right-left)//2)  # 防止溢出，等同于(left + right) / 2
                if nums[mid] < target:
                    # left = mid
                    left = mid+1
                elif nums[mid] > target:
                    # right = mid
                    right = mid-1
                else:
                    return mid
            else:
                return -1


"""
写二分法，区间的定义一般为两种，左闭右闭即[left, right]，或者左闭右开即[left, right)。
@1 左闭右闭时，写 left <= right && right = mid-1，因为此时右区间是有意义的
@2 左闭右开时，写 left < right && right = mid，因为此时右区间无意义；
"""


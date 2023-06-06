from typing import List

"""
这个题用暴力求解就是先平方，再排序；
如果采用双指针法的话，就是依次在最左端和最右端进行判断，然后逐渐缩小范围
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = k = len(nums)-1
        lenth = len(nums)
        # res = []
        res = [-1] * lenth
        while left <= right:
            lm = nums[left] ** 2
            rm = nums[right] ** 2
            if lm < rm:
                res[k] = rm
                right -= 1
            else:
                res[k] = lm
                left += 1
            k -= 1
        return res


from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, key=abs, reverse=True)  # 将nums按照abs降序排列
        for i in range(len(nums)):  # 第一步，将nums中的所有负数转换为正数
            if k > 0 and nums[i] < 0:
                nums[i] *= -1
                k -= 1

        if k > 0:  # 第二步，此时nums已经变为全正数，因此取数组中最小的数组进行反转，可保证全局最大
            nums[-1] *= ((-1) ** k)

        return sum(nums)


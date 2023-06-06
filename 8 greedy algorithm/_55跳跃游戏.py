from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        若存在元素为0，且非数组结尾处，则无法到达最后一个下标。
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return True
        cover, i = 0, 0
        while i <= cover:  # 判断当前是否还在cover范围内
            cover = max(i + nums[i], cover)  # 根据当前遍历到的元素值实时更新cover
            if cover >= len(nums)-1:
                return True
            i += 1
        return False  # 如果在当前cover内仍无法到达最后一个下标，则false

    nums = [2, 0, 0]
    res = canJump(object, nums=nums)
    print(res)

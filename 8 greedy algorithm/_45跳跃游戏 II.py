from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        同时统计当前最大覆盖和下一步最大覆盖
        若当前最大覆盖无法达到最后一个下标，则再走一步
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 0

        ans = 0
        curDistance, nextDistance = 0, 0
        for i in range(len(nums)):  # 遍历nums数组
            nextDistance = max(i + nums[i], nextDistance)  # 判断下一步遍历的范围
            if i == curDistance:  # 遇到当前覆盖最远距离下标
                if curDistance < len(nums)-1:  # 如果当前可移动范围小于nums长度，说明还需要再移动一步
                    ans += 1
                    curDistance = nextDistance  # 更新当前可移动范围
                    if nextDistance >= len(nums)-1:  # 如果下一步可移动范围大于nums长度，说明下一次移动可以达到终点
                        break  # 退出循环
                else:
                    break  # 当前可移动范围大于nums长度，可达到终点，直接退出循环

        return ans

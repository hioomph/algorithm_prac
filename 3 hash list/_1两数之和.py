from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        # 遍历nums的key和val，若在record中存在target-val这个键，则返回其值（对应原nums的索引），否则向record中新添加元素
        for key, val in enumerate(nums):
            if target - val in record:
                return [record[target - val], key]
            else:
                record[val] = key



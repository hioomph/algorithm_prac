from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {}
        ans = []

        # 遍历nums1
        for num in nums1:
            record[num] = 1 # 设定为1是为了满足结果中元素的唯一性

        # 遍历nums2
        for num in nums2:
            if num in record.keys() and record[num] == 1:
                ans.append(num)
                record[num] += 1  # 保证ans中元素的唯一性
        return ans
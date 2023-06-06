from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = {}
        count = 0

        for i in nums1:
            for j in nums2:
                if i+j not in record.keys():
                    record[i+j] = 1
                else:
                    record[i+j] += 1

        for i in nums3:
            for j in nums4:
                if 0-(i+j) in record.keys():
                    count += record[0-(i+j)]

        return count


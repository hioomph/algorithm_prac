from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key=lambda x: (x[0]))
        # intervals = sorted(intervals, key=lambda x: (x[1]))  # 错误
        end = intervals[0][1]
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last = res[-1]  # last为res中的最后一个区间，也即是当前最右边的区间
            if last[1] >= intervals[i][0]:  # 两个区间重叠
                res[-1] = [min(last[0], intervals[i][0]), max(last[1], intervals[i][1])]
            else:  # 如果last的右边界小于下一个待比较区间的左边界，说明二者不重叠
                res.append(intervals[i])

        return res
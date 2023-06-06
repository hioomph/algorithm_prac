from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        res = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:
                res += 1
                end = intervals[i][1]

        return len(intervals) - res



    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    res = eraseOverlapIntervals(object, intervals)
    print(res)
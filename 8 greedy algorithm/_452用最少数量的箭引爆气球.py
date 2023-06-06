from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 对二维数组排序
        points.sort(key=lambda x: x[0])
        # points = [[10,16],[2,8],[1,6],[7,12]]  ==>  [[1, 6], [2, 8], [7, 12], [10, 16]]

        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])  # 更新重叠气球最小右边界
        return result





    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    res = findMinArrowShots(object, points)


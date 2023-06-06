from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx = starty = 0  # 每一行、列的起始索引
        mid = n // 2  # 判断是否存在中心点
        loop = n // 2  # 判断存在几圈
        res = [[0] * n for _ in range(n)]
        count = 1

        # for offset in range(1, loop):
        for offset in range(1, loop+1):
            # 从左至右
            for i in range(starty, n - offset):
                res[startx][i] = count
                count += 1
            # 从上至下
            for j in range(startx, n - offset):
                res[j][n - offset] = count
                count += 1
            # 从右至左
            # for i in range(starty, n - offset, -1):
            # range(start, stop[, step])，所以此处要倒数时注意起始为starty，而终止为n-offset
            for i in range(n - offset, starty, -1):
                res[n - offset][i] = count
                count += 1
            # 从下至上
            # for j in range(startx, n - offset, -1):
            for j in range(n - offset, startx, -1):
                # res[j][n - offset] = count
                res[j][starty] = count
                count += 1
            startx += 1
            starty += 1

        if n % 2:
            res[mid][mid] = n * n

        return res
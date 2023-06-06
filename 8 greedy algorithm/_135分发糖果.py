from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        这道题的关键在于不能同时考虑左>右和右>左两种情况，而是要分开考虑
        一种解题顺序是：
            step1：评分右>左，此时从前往后遍历
            step2：评分左>右，此时从后往前遍历
            【step1 & 2的顺序可交换】
        :param ratings:
        :return:
        """
        res = [1] * len(ratings)
        # step1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        # step2
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # res[i] = res[i+1] + 1  # 没有在step1的基础上进行改动
                res[i] = max(res[i+1] +1, res[i])

        return sum(res)

    ratings = [1, 3, 4, 5, 2]
    res = candy(object, ratings)
    print(res)
    
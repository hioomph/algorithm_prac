from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        局部最优：收集每天的正利润，全局最优：求得最大利润
        """

        profit = [0] * (len(prices)-1)
        res = 0

        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            profit[i-1] = tmp
            if profit[i-1] > 0:
                res += profit[i-1]

        return res

    prices = [7,1,5,3,6,4]
    res = maxProfit(object, prices)
    print(res)

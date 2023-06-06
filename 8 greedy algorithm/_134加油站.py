from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rest = [0] * len(gas)
        curSum = 0
        totalSum = 0
        index = 0  # 最终返回的结果
        for i in range(len(gas)):
            rest[i] = gas[i] - cost[i]  # rest表示在第i个加油站的油量结余，注意是gas-cost，顺序很重要
            curSum += rest[i]  # 计算当前总剩余
            totalSum += rest[i]  # 计算总剩余
            if curSum < 0:  # 如果当前总剩余小于0，说明起始点不能选在[0,i]的范围内，因为无论怎么选都会最终为负，走不到
                index = i + 1  # 起始点只能从i+1开始选
                curSum = 0  # 更新curSum为0
        if totalSum < 0:  # 若总油量小于总消耗，这条路是跑不通的，直接返回-1
            return -1
        return index

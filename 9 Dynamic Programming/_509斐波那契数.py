class Solution:
    def fib(self, n: int) -> int:
        # 动态规划实现版
        if n == 0:
            return 0

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

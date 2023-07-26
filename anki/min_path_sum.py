class Solution(object):
    def minPathSum(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        dp = []
        for _ in range(len(grid)):
            dp.append([0] * len(grid[0]))

        dp[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, len(grid[0])):
            dp[0][j] = grid[0][j] + dp[0][j-1]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])

        return dp[-1][-1]



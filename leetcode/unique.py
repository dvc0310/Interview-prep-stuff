class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0]* n for _ in range(m)]

        for i in range(n):
            dp[m-1][i] = 1

        for i in range(m-1):
            dp[i][n-1] = 1

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                dp[row][col] = dp[row+1][col] + dp[row][col+1]

        return dp[0][0]

        """
        :type m: int
        :type n: int
        :rtype: int
        """
m = 3
n = 7
print(Solution().uniquePaths(m, n))
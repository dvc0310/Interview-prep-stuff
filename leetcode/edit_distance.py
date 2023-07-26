class Solution(object):
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)

        # Initialize a (m+1) * (n+1) matrix dp
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        # Base cases: transform empty word1 to word2
        for i in range(n+1):
            dp[0][i] = i

        # Base cases: transform word1 to empty word2
        for i in range(m+1):
            dp[i][0] = i

        # For each pair of characters in word1 (i) and word2 (j)
        for i in range(1, m+1):
            for j in range(1, n+1):
                # If the characters match, no operation needed
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Min among replace, remove and add
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        # The value in dp[m][n] is the minimum distance
        return dp[m][n]

word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))
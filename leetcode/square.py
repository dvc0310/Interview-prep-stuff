
class Solution(object):
    def maximalSquare(self, matrix):
        found = True
        max_square = 1
        height = len(matrix)
        width = len(matrix[0])
        dp = [[0]*(width-1) for _ in range(height-1)]
        for i in range(1, height):
            for j in range(1, width):
                if self.foundSquare(matrix, i, j):
                    dp[i-1][j-1] = str(int(matrix[i][j]) + 1)
                    max_square = max(int(matrix[i][j]) ** 2, max_square)
                    found = True
         
        return max_square
            
    def foundSquare(self, matrix, row, col):
        return matrix[row][col] == matrix[row][col - 1] and \
            matrix[row][col] == matrix[row - 1][col - 1] and \
            matrix[row][col] == matrix[row - 1][col] and \
            matrix[row][col] != str(0)

class Solution2(object):
    def maximalSquare(self, matrix):
        if matrix is None or len(matrix) < 1:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        
        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1
                    max_side = max(max_side, dp[r+1][c+1])
        
        return max_side * max_side



matrix = [["1","1","1","1","1"],
          ["1","1","0","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["1","1","1","1","0"]]
print(Solution2().maximalSquare(matrix))
matrix = [["1","1"],["1","1"]]
print(Solution2().maximalSquare(matrix))


class Solution3(object):
    def maxKilledEnemies(self, grid):
        dp = [[0]*(len(grid[0])) for _ in range(len(grid))]
        rowhit = 0
        colhit = len(grid[0]) * [0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                k = j
                l = i
                if (grid[i][j-1] == 'W' or j == 0):
                    rowhit = 0
                    while k < len(grid[i]) and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            rowhit += 1
                        k += 1
                if (grid[i-1][j] == 'W' or i == 0):
                    colhit[j] = 0
                    while l < len(grid) and grid[l][j] != 'W':
                        if grid[l][j] == 'E':
                            colhit[j] += 1
                        l += 1
                if grid[i][j] == '0':
                    dp[i][j] = rowhit + colhit[j]
        return dp
        

matrix = [['W', 'E', '0', 'W', 'E', '0'], 
          ['E', 'E', '0', 'W', '0', 'E'], 
          ['0', 'E', '0', '0', 'E', '0'], 
          ['W', '0', 'E', 'W', '0', 'E'],
          ['0', 'W', '0', 'E', 'W', '0'], 
          ['E', '0', 'W', '0','E', 'W']]
print(Solution3().maxKilledEnemies(matrix))
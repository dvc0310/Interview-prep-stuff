class Solution(object):
    def bestTeamScore(self, ages, scores):
        if not scores:
            return 0
        
        lst = [0] * len(ages)
        dp = [0] * len(ages)
        
        for i in range(len(scores)):
            lst[i] = (scores[i], ages[i])

        lst.sort(key=lambda x: (x[1], x[0]))
        scores = [pair[0] for pair in lst]
        dp[0] = scores[0]
        for current in range (1, len(scores)):
            dp[current] = scores[current]
            for previous in range(0, current):
                if scores[current] >= scores[previous]:
                    dp[current] = max(dp[current], dp[previous] + scores[current])

        return max(dp)
    
    def bestTeamScore2(self, ages, scores):
        players = sorted(zip(scores, ages))
        n = len(players)
        dp = [0] * n
        for i in range(n):
            dp[i] = players[i][0]
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][0])
        return max(dp)
    

    
print(Solution().bestTeamScore([3,4,5,5,5,6,6,6,7,7], [2,3,1,7,8,5,6,20,12,20]))

# Sure, here is the renamed code:

class Solution(object):
    def maxKilledEnemies(self, grid):
        max_kills = 0
        row_hits = 0
        col_hits = [0] * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                temp_col = col
                temp_row = row
                if (grid[row][col-1] == 'W' or col == 0):
                    row_hits = 0
                    while temp_col < len(grid[row]) and grid[row][temp_col] != 'W':
                        if grid[row][temp_col] == 'E':
                            row_hits += 1
                        temp_col += 1
                if (grid[row-1][col] == 'W' or row == 0):
                    col_hits[col] = 0
                    while temp_row < len(grid) and grid[temp_row][col] != 'W':
                        if grid[temp_row][col] == 'E':
                            col_hits[col] += 1
                        temp_row += 1
                if grid[row][col] == '0':
                    max_kills = max(max_kills, row_hits + col_hits[col])
        return max_kills



        
grid = [["0","E","0","0"],
        ["E","0","W","E"],
        ["0","E","0","0"]]
print(Solution().maxKilledEnemies(grid))



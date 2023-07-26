def minpathsum(grid):
    rows = len(grid)
    cols = len(grid[0])
    dp = []
    edgeTo = []
    for i in range(len(grid)):
        dp.append(cols*[0])
        edgeTo.append(cols*[(-1, -1)])
    
    dp[0][0] = grid[0][0]

    for i in range(1, cols):
        dp[0][i] = dp[0][i-1] + grid[0][i]
        edgeTo[0][i] = (i - 1, 0)
    
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
        edgeTo[i][0] = (0, i - 1)

    for i in range(1, rows):
        for j in range(1, cols):
            up = dp[i-1][j]
            upindex = (j, i-1)
            left = dp[i][j-1]
            leftindex = (j-1, i)
            if up + grid[i][j] < left + grid[i][j]:
                dp[i][j] = up + grid[i][j]
                edgeTo[i][j] = upindex
            else:
                dp[i][j] = left + grid[i][j]
                edgeTo[i][j] = leftindex
    
    curr = edgeTo[rows-1][cols-1]
    path = [grid[rows-1][cols-1]]
    while curr != (-1,-1):
        path.append(grid[curr[1]][curr[0]])
        curr = edgeTo[curr[1]][curr[0]]
    
    path.reverse()

    return dp[-1][-1]


print(minpathsum([[1,3,1,19],
                  [1,5,1,14],
                  [4,2,1,1]]))
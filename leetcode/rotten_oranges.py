from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        if len(grid) == 0:
            return -1
        
        sources = deque()
        zerocount = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 0:
                    zerocount += 1
                if grid[row][col] == 2:
                    sources.append((row, col, 0))
        if zerocount == len(grid) * len(grid[0]):
            return 0 
        return self.bfs(grid, sources)
    
    def bfs(self, grid, sources):
        current_minute = 0
        if not sources:
            return -1
        while sources:
            row, col, minute = sources.popleft()
            current_minute = max(minute, current_minute)
            for neighborRow, neighborCol in self.neighbors(grid, row, col):
                if grid[neighborRow][neighborCol] == 1:
                    grid[neighborRow][neighborCol] = 2
                    sources.append((neighborRow, neighborCol, minute + 1))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return current_minute
    
    def neighbors(self, grid, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lst = []
        for v, h in directions:
            newRow = row + v
            newCol = col + h
            if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[row]):
                lst.append((newRow, newCol))
        return lst

grid = [[0]]

print(Solution().orangesRotting(grid))
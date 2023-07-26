class Island:                    
    def countIslandsDFS(self, matrix):
        count = 0
        visited = [[False]*len(row) for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not visited[i][j]: 
                    self.islandSizeDFS(matrix, j, i, visited)
                    count += 1
        return count
    
    def countClosedIslands(self, matrix):
        countClosedIslands = 0
        countaOpenIslands = 0
        visited = [[False]*len(row) for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not visited[i][j]: 
                    countaOpenIslands += self.closedIslandDFS(matrix, j, i, visited)
                    countClosedIslands += 1
        return countClosedIslands - countaOpenIslands
    
    def getIslandSizes(self, matrix):
        lst = []
        visited = [[False]*len(row) for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not visited[i][j]: 
                    lst.append(self.islandSizeDFS(matrix, j, i, visited))
        return lst
    
    def isPositionValid(self, matrix, visited, x, y):
        return 0 <= y < len(matrix) and \
        0 <= x < len(matrix[y]) and not visited[y][x] and matrix[y][x] == 1
    
    def neighbors(self, x, y, directions, matrix, visited):
        lst = []
        for direction in directions:
            if self.isPositionValid(matrix, visited, x + direction[1], y + direction[0]):
                lst.append((y + direction[0], x + direction[1]))
        return lst
    
    def allNeighbors(self, x, y, directions, matrix):
        count = 0
        for direction in directions:
            if 0 <= y + direction[0] < len(matrix) and 0 <= x + direction[1] < len(matrix[y]):
                count += 1
        return count

    def islandSizeDFS(self, matrix, x, y, visited):
        right, left, up, down = (0, 1), (0, -1), (-1, 0), (1, 0)
        directions = [right, left, up, down]
        stack = [(y, x)]
        
        islandSize = 0

        while stack:
            y, x = stack.pop()
            if not visited[y][x]: 
                visited[y][x] = True
                neighbors = self.neighbors(x, y, directions, matrix, visited)
                for neighbor in neighbors:
                    if not visited[neighbor[0]][neighbor[1]]:
                        stack.append(neighbor)
                islandSize += 1
        return islandSize
    
    def closedIslandDFS(self, matrix, x, y, visited):
        right, left, up, down = (0, 1), (0, -1), (-1, 0), (1, 0)
        directions = [right, left, up, down]
        stack = [(y, x)]
        isClosed = True

        while stack:
            y, x = stack.pop()
            if not visited[y][x]: 
                visited[y][x] = True
                neighbors = self.neighbors(x, y, directions, matrix, visited)
                allNeighbors = self.allNeighbors(x, y, directions, matrix)
                if allNeighbors < 4:
                    isClosed = False
                for neighbor in neighbors:
                    if not visited[neighbor[0]][neighbor[1]]:
                        stack.append(neighbor)
        if not isClosed:
            return 1
        return 0
    
    def perimeterCount(self, x, y, directions, matrix):
        count = 0
        for direction in directions:
            newY = y + direction[0]
            newX = x + direction[1]
            if not (0 <= newY < len(matrix)) or not (0 <= newX < len(matrix[0])) or matrix[newY][newX] == 0:
                count += 1
        return count

    def islandPerimeterDFS(self, matrix, x, y, visited):
        right, left, up, down = (0, 1), (0, -1), (-1, 0), (1, 0)
        directions = [right, left, up, down]
        stack = [(y, x)]
        
        perimeter = 0

        while stack:
            y, x = stack.pop()
            if not visited[y][x]: 
                visited[y][x] = True
                perimeter += self.perimeterCount(x, y, directions, matrix)
                for neighbor in self.neighbors(x, y, directions, matrix, visited):
                    if not visited[neighbor[0]][neighbor[1]]:
                        stack.append(neighbor)
                
        return perimeter
    
    def findIslandPerimeter(self, matrix):
        perimeter = 0
        visited = [[False]*len(row) for row in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not visited[i][j]: 
                    return self.islandPerimeterDFS(matrix, j, i, visited)
                    
        return perimeter

    
matrix = [[1,1,0,0,0],
          [0,1,0,0,0],
          [0,1,0,0,0],
          [0,1,1,0,0],
          [0,0,0,0,0]]

print(Island().countIslandsDFS(matrix))
print(Island().getIslandSizes(matrix))
print(Island().countClosedIslands(matrix))
print(Island().findIslandPerimeter(matrix))
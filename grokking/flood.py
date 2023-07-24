class Flood:
    def floodFill(self, matrix, y, x, newColor):
        visited = [[False]*len(row) for row in matrix]
        oldColor = matrix[y][x]
        self.dfs(matrix, x, y, visited, newColor, oldColor)
        return matrix

    def dfs(self, matrix, x, y, visited, newColor, oldColor):
        stack = [(y, x)]
        while stack:
            y, x = stack.pop()
            if not visited[y][x]: 
                visited[y][x] = True    # mark as visited as soon as it's popped
                matrix[y][x] = newColor  # change its color as soon as it's popped
                for neighbor in self.neighbors(matrix, x, y, visited, oldColor):
                    if not visited[neighbor[0]][neighbor[1]]:
                        stack.append(neighbor)

    def checkValid(self, matrix, x, y, visited, oldColor):
        return (0 <= y < len(matrix)) and \
               (0 <= x < len(matrix[y])) and \
               not visited[y][x] and \
               matrix[y][x] == oldColor

    def neighbors(self, matrix, x, y, visited, oldColor):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        lst = []
        for direction in directions:
            newX = x + direction[0]
            newY = y + direction[1]
            if self.checkValid(matrix, newX, newY, visited, oldColor):
                lst.append((newY, newX))
        return lst


matrix = [[0,1,1,1,0],
          [0,0,0,1,1],
          [0,1,1,1,0],
          [0,1,1,0,0],
          [0,0,0,0,0]]

print(Flood().floodFill([[1,2,1],
                         [0,1,0],
                         [1,2,1]], 0, 1, 3))
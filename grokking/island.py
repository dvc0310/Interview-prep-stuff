class Island:  
    def isPositionValid(self, matrix, visited, x, y):
        return 0 <= y < len(matrix) and \
        0 <= x < len(matrix[y]) and not visited[y][x] and matrix[y][x] == 1
    
    def neighbors(self, x, y, directions, matrix, visited):
        lst = []
        for direction in directions:
            if self.isPositionValid(matrix, visited, x + direction[0][1], y + direction[0][0]):
                lst.append((y + direction[0][0], x + direction[0][1], direction[1]))
        return lst

    def pathDFS(self, matrix, x, y, visited):
        right, left, up, down = (0, 1), (0, -1), (-1, 0), (1, 0)
        directions = [(right, "r"), (left, "l"), (up, "u"), (down, "d")]
        stack = [(y, x, "s")]
        path = []
        my_key = ''.join(map(str, ""))

        while stack:
            y, x, dir = stack.pop()
            if not visited[y][x]: 
                visited[y][x] = True
                path.append(dir)
                my_key = '|'.join(map(str, path))
                neighbors = self.neighbors(x, y, directions, matrix, visited)
                for neighbor in neighbors:
                    if not visited[neighbor[0]][neighbor[1]]:
                        stack.append(neighbor)
                
        return my_key
    
    def countDistinctIslandsDFS(self, matrix):
        visited = [[False]*len(row) for row in matrix]
        my_dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1 and not visited[i][j]: 
                    key = self.pathDFS(matrix, j, i, visited)
                    if key not in my_dict:
                        my_dict[key] = 1
                    else:
                        my_dict[key] += 1
        return len(my_dict)
    
matrix = [[1,1,0,1,1],
          [1,1,0,1,1],
          [0,0,0,0,0],
          [0,1,1,0,1],
          [0,1,1,0,1]]
matrix2 = [[1,1,0,1],
           [0,1,1,0],
           [0,0,0,0],
           [1,1,0,0],
           [0,1,1,0]]

print(Island().countDistinctIslandsDFS(matrix2))
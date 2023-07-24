class Island:                    
    def countIslandsDFS(self, matrix):
        totalIslands = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:  
                    totalIslands += 1
                    self.visitIslandDFS(matrix, i, j)
        return totalIslands

    def isPositionValid(self, matrix, x, y):
        if 0 <= y < len(matrix) and \
              0 <= x < len(matrix[y]) and \
                  matrix[x][y] == 1:
            return True
        return False

    def visitIslandDFS(self, matrix, x, y):
        # Each pair in directions corresponds to a cardinal direction: right, left, down, and up.
        right, left, down, up = (0, 1), (0, -1), (1, 0), (-1, 0)
        cardinalDirections = [right, left, down, up]  
        
        # We're using a stack to track the positions we need to visit.
        positionsToVisit = [(x, y)] 

        while positionsToVisit:
            x, y = positionsToVisit.pop()
            if self.isPositionValid(matrix, x, y):
                for xShift, yShift in cardinalDirections:
                    newX, newY = x + xShift, y + yShift
                    if self.isPositionValid(matrix, newX, newY):
                        positionsToVisit.append((newX, newY))  
            
            matrix[x][y] = 0

matrix = [[1,1,1,0,0],[0,1,0,0,1],[0,0,1,1,0],[0,0,1,0,0],[0,0,1,0,0]]
print(Island().countIslandsDFS(matrix))

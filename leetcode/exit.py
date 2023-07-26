from collections import deque
class Solution(object):
    def neighbors(self, row, col, maze):
        lst = []
        if col + 1 < len(maze[0]) and maze[row][col + 1] != "+":
            lst.append([row, col + 1])  
        if col - 1 >= 0 and maze[row][col - 1] != "+":
            lst.append([row, col - 1])
        if row + 1 < len(maze) and maze[row + 1][col] != "+":
            lst.append([row + 1, col])
        if row - 1 >= 0 and maze[row - 1][col] != "+":
            lst.append([row - 1, col])
        return lst

    def nearestExit(self, maze, entrance):
        edgeTo = [[None] * len(maze[0]) for _ in range(len(maze))] 

        queue = deque()
        queue.append(entrance)
        path = []
        visited = set()
        visited.add(entrance)

        while queue:
            v = queue.popleft()
            if v != entrance and (0 in v or v[0] == len(maze) - 1 or v[1] == len(maze[0]) - 1):
                curr = v
                while curr != entrance:
                    path.append(curr)
                    curr = edgeTo[curr[0]][curr[1]]
                path.append(curr)
                return len(path)
            else:
                for neighbor in self.neighbors(v[0], v[1], maze):
                    if neighbor not in visited:
                        edgeTo[neighbor[0]][neighbor[1]] = v
                        visited.add(neighbor)
                        queue.append(neighbor)
       
        return - 1


class Solution2(object):
    def neighbors(self, row, col, maze):
        lst = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(maze) and \
                0 <= new_col < len(maze[0]) and maze[new_row][new_col] != "+":
                lst.append([new_row, new_col])
        return lst

    def nearestExit(self, maze, entrance):
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        visited = set()
        queue = deque([(entrance, 0)])
        if entrance[0] in [0, len(maze)-1] or entrance[1] in [0, len(maze[0])-1]:
            return 0
        while queue:
            cur, steps = queue.popleft()
            x, y = cur[0], cur[1]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx >= 0 and nx < len(maze) and ny >= 0 and \
                    ny < len(maze[0]) and maze[nx][ny] != '+' and (nx, ny) not in visited:
                    if nx == 0 or ny == 0 or nx == len(maze)-1 or ny == len(maze[0])-1:                       
                        return steps+1
                    queue.append(((nx, ny), steps+1))
                    visited.add((nx, ny))

        return -1



maze = [["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."],
        [".", ".", ".", "+"],
        ["+", ".", ".", "."]]

entrance = [0,2]
print(Solution().nearestExit(maze, entrance))
entrance = [1,2]
print(Solution().nearestExit(maze, entrance))
entrance = [3,0]
print(Solution().nearestExit(maze, entrance))

maze = [["+", "+", "+", "+", "+", ".", "+", "+", "+"],
        [".", ".", ".", ".", ".", ".", ".", ".", "+"],
        ["+", "+", "+", "+", "+", "+", "+", "+", "+"],
        [".", "+", ".", ".", ".", ".", ".", ".", "."],
        [".", "+", ".", ".", "+", "+", ".", "+", "."],
        [".", "+", ".", ".", ".", ".", ".", "+", "."],
        ["+", "+", "+", ".", "+", "+", "+", "+", "+"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."]]
entrance = [3,3]
print(Solution().nearestExit(maze, entrance))

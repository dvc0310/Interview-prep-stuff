class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        stack = [0]
        count = 0
        while stack:
            v = stack.pop()
            visited[v] = True
            count += 1
            for neighbor in rooms[v]:
                if not visited[neighbor] and neighbor not in stack:
                    stack.append(neighbor)

        return count == len(rooms)


rooms = [[1, 2, 3],[3, 0],[1, 3],[0]]
print(Solution().canVisitAllRooms(rooms))
rooms = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms(rooms))
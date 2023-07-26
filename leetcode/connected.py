class Solution(object):
    def findCircleNum2(self, isConnected):
        size = [1] * len(isConnected)
        parents = list(range(len(isConnected)))
        provinces = len(isConnected)

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        
        def union(node1, node2, provinces):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:
                provinces -= 1
                if size[root1] > size[root2]:
                    size[root1] += size[root2]
                    parents[root2] = root1
                else:
                    size[root2] += size[root1]
                    parents[root1] = root2
            return provinces

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i != j and isConnected[i][j] == 1:
                    provinces = union(i, j, provinces)
                if provinces == 1:
                    return provinces
        
        return provinces


    def findCircleNum(self, isConnected):
        def DFS(start, visited):
            stack = [start]
            
            while stack:
                v = stack.pop()
                visited[v] = True
                for i in range(len(isConnected)):
                    if i != v and not visited[i] and isConnected[v][i] == 1:
                        stack.append(i)
                        
        visited = [False] * len(isConnected)
        count = 0
        for i in range(len(visited)):
            if not visited[i]:
                count += 1
                DFS(i, visited)

        return count
                 

matrix4 = [
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

print(Solution().findCircleNum2(matrix4))
print(Solution().findCircleNum2([[1,0,0],[0,1,0],[0,0,1]]))

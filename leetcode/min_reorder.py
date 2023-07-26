from collections import defaultdict
class Solution(object):
    def minReorder(self, n, connections):
        graph = {}
        zeros = {}
        visited = {}
        for i in range(len(connections)):
            if connections[i][0] not in graph:
                graph[connections[i][0]] = []
                zeros[connections[i][0]] = False
                visited[connections[i][0]] = False
            if connections[i][1] not in graph:
                graph[connections[i][1]] = []
                zeros[connections[i][1]] = False
                visited[connections[i][1]] = False
                
        for edge in connections:
            graph[edge[0]].append(edge[1])
       
        for key in graph.keys():
            zeros[key] = self.hasPathZero(key, graph)

        count = 0
        for key, value in zeros.items():
            if not value:
                for neighbor in graph[key]:
                    if zeros[neighbor]:
                        zeros[key] = True
                        value = True
                        break
            if value:
                count += self.zerodfs(graph, key, visited, zeros)
                 
        return count
    

    def hasPathZero(self, start, graph):
        stack = [start]
        visited = set()
        while stack:
            v = stack.pop()
            visited.add(v)
            if v == 0:
                return True
            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False


    def zerodfs(self, graph, start, visited, zeros):
        stack = [start]
        count = 0
        while stack:
            v = stack.pop()
            visited[v] = True
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)
                    if not zeros[neighbor]:
                        count += 1
                        zeros[neighbor] = True
        return count
            

class OptimalSolution:
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        roadSet = set()

        # Build the graph and roadSet.
        for road in connections:
            u, v = road
            graph[u].append(v)
            graph[v].append(u)
            roadSet.add((u, v))

        return self.dfs(0, graph, roadSet)

    def dfs(self, start, graph, roadSet):
        counter = 0
        stack = [(start, -1)]  # node and parent

        while stack:
            node, parent = stack.pop()
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if (node, neighbor) in roadSet:
                    counter += 1
                stack.append((neighbor, node))

        return counter

class OptimalSolution2:
    def minReorder(n, connections):
        graph = {i: [] for i in range(n)}
        for u, v in connections:
            graph[u].append((v, False))  # Edge from u to v is not valid
            graph[v].append((u, True))   # Edge from v to u is valid
        
        stack = [(0, None)]
        visited = set()
        changes = 0
        
        while stack:
            node, valid = stack.pop()
            if node not in visited:
                visited.add(node)
                if valid == False:
                    changes += 1
                for neigh, valid in graph[node]:
                    if neigh not in visited:
                        stack.append((neigh, valid))
        return changes



n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Solution().minReorder(n, connections)
OptimalSolution().minReorder(n, connections)
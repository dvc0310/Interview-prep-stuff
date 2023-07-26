def coins(n):
    start = 0
    end = n
    
    while end >= start:
        mid = start + (end - start) // 2
        x = mid * (mid + 1) // 2
        if x > n:
            end = mid - 1
        elif x < n:
            start = mid + 1
        else:
            return x
    return end

class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = {}

        # Initialize the graph with empty lists for each node
        for u, v in equations:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

        for i, edge in enumerate(equations):
            u, v = edge
            graph[u].append((v, values[i]))  
            graph[v].append((u, 1/values[i]))   

        lst = []
        for start, end in queries:
            if start not in graph.keys() or end not in graph.keys():
                lst.append(float(-1))
            else:
                lst.append(self.dfs(start, end, graph))
        return lst
    
    def dfs(self, start, end, graph):
        visited = {node: False for node in graph.keys()}
        stack = [(start, 1, 1)]

        while stack:
            toNode, cost, count = stack.pop()
            count = count * cost
            visited[toNode] = True
            if toNode == end:
                return float(count)
            for neighbor in graph[toNode]:
                if not visited[neighbor[0]]:
                    stack.append((neighbor[0], neighbor[1], count))
        return float(-1)

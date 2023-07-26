
from collections import deque

def numSquares(n):
    queue = deque([(n, 0)])

    while queue:
        node, depth = queue.popleft()

        if node == 0:
            return depth
        val = int(node**0.5) + 1
        for i in range(1, val):
            new_node = node - i**2
            if new_node not in queue:
                queue.append((new_node, depth + 1))

def graph_to_str(n):
    graph_str = []
    for i in range(n+1):
        neighbors = [i - j**2 for j in range(1, int(i**0.5)+1)]
        graph_str.append(f"{i} --{neighbors}-->")
    return '\n'.join(graph_str)



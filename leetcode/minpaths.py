
def traverse_graph_from_bottom_right(graph):
    rows = len(graph)
    columns = len(graph[0])

    # Start from the bottom right element
    i = rows - 1
    j = columns - 1

    traversing_path = []

    while i >= 0 and j >= 0:
        traversing_path.append(graph[i][j])

        # If we're not at the top or the left, go in the direction of smaller number
        if i > 0 and j > 0:
            if graph[i - 1][j] < graph[i][j - 1]:
                i -= 1
            else:
                j -= 1
        # If we're at the top, only way is left
        elif j > 0:
            j -= 1
        # If we're at the left, only way is up
        else:
            i -= 1

    return traversing_path

graph = [[1,3,1],[1,5,1],[1,2,1]]
print(traverse_graph_from_bottom_right(graph))

            
            
        
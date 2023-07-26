
def hasCycle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if (not visited[i][j]):  # only if the cell is not visited
                if (containsCycleDFS(matrix, visited, matrix[i][j], i, j, -1, -1)):
                    return True
    return False


def containsCycleDFS(matrix, visited, startChar, x,  y, prevX, prevY):
    if (x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0])):
        return False  # not a valid cell

    if (matrix[x][y] != startChar):
        return False  # different character which means a different island

    if (visited[x][y]):
        return True  # found a cycle, as we are visiting an already visited valid cell

    visited[x][y] = True  # mark the cell visited

    # recursively visit all neighboring cells (horizontally & vertically)
    if (x + 1 != prevX and containsCycleDFS(matrix, visited, startChar, x + 1, y, x, y)): # down
        return True
    if (x - 1 != prevX and containsCycleDFS(matrix, visited, startChar, x - 1, y, x, y)): # up
        return True
    if (y + 1 != prevY and containsCycleDFS(matrix, visited, startChar, x, y + 1, x, y)): # right
        return True
    if (y - 1 != prevY and containsCycleDFS(matrix, visited, startChar, x, y - 1, x, y)): # left
        return True

    return False


def main():
    print(hasCycle([['a', 'a', 'a', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'c', 'a'],
                    ['b', 'a', 'a', 'a']]))

    print(hasCycle([['a', 'a', 'a', 'a'],
                    ['a', 'b', 'b', 'a'],
                    ['a', 'b', 'a', 'a'],
                    ['a', 'a', 'a', 'c']]))

    print(hasCycle([['a', 'b', 'e', 'b'],
                    ['b', 'b', 'b', 'b'],
                    ['b', 'c', 'c', 'd'],
                    ['c', 'c', 'd', 'd']]))


main()

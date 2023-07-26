import heapq

def minPathSum_graph(grid):
    rows = len(grid)
    cols = len(grid[0])

    directions = [(0, 1), (1, 0)]

    distances = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(float('inf'))
        distances.append(row)

    distances[0][0] = grid[0][0]

    queue = [(grid[0][0], 0, 0)]

    while queue:
        current_dist, current_row, current_col = heapq.heappop(queue)

        if current_dist != distances[current_row][current_col]:
            continue

        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc

            if 0 <= next_row < rows and 0 <= next_col < cols:
                neighbor_val = grid[next_row][next_col]
                new_distance = current_dist + neighbor_val

                if new_distance < distances[next_row][next_col]:
                    distances[next_row][next_col] = new_distance
                    heapq.heappush(queue, (new_distance, next_row, next_col))

    return distances[-1][-1]

def minimum_path_sum(grid):
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])

    minimum_sum_grid = []
    for _ in range(number_of_rows):
        minimum_sum_grid.append([0] * number_of_columns)

    minimum_sum_grid[0][0] = grid[0][0]

    for column in range(1, number_of_columns):
        sum_of_previous_column = minimum_sum_grid[0][column - 1]
        current_grid_value = grid[0][column]
        minimum_sum_grid[0][column] = sum_of_previous_column + current_grid_value

    for row in range(1, number_of_rows):
        sum_of_previous_row = minimum_sum_grid[row - 1][0]
        current_grid_value = grid[row][0]
        minimum_sum_grid[row][0] = sum_of_previous_row + current_grid_value

    for row in range(1, number_of_rows):
        for column in range(1, number_of_columns):
            sum_of_above_cell = minimum_sum_grid[row - 1][column]
            sum_of_left_cell = minimum_sum_grid[row][column - 1]
            current_grid_value = grid[row][column]
            minimum_sum_grid[row][column] = min(sum_of_above_cell, sum_of_left_cell) + current_grid_value

    return minimum_sum_grid[-1][-1]

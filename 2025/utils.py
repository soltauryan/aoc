def return_surrounding_coord(grid, row, col):
    grid_row_max_len = len(grid) - 1
    grid_col_max_len = len(grid[0]) - 1
    coord_set = set()
    for row_i in range(row-1, row+2):
        for col_i in range(col-1, col+2):
            if row_i < 0 or col_i < 0 or row_i > grid_row_max_len or col_i > grid_col_max_len:
                continue
            elif row_i == row and col_i == col:
                continue
            else:
                coord_set.add((row_i, col_i))


    return coord_set

def get_neighbourhood(n_type, mat, coordinates):
    row_number = coordinates[0]
    column_number = coordinates[1]
    if n_type == 'moore':
        from itertools import product, starmap
        height, width = len(mat), len(mat[0])
        if row_number > height-1 or column_number > width-1:
            result = []
        else:
            cells = list(starmap(lambda a, b: (row_number + a, column_number + b), product((0, -1, +1), (0, -1, +1))))
            cells.pop(0)
            coords = list(filter(lambda cell: cell[0] in range(height) and cell[1] in range(width), cells))
            result = []
            for coord in coords:
                result.append(mat[coord[0]][coord[1]])

    else:    # 'von_neumann'
        if len(mat) == 1:
            result = []
        else:
            height, width = len(mat), len(mat[0])
            if row_number > height-1 or column_number > width-1:
                result = []
            else:
                if row_number == 0 or row_number == len(mat) - 1 or column_number == 0 or column_number == len(mat[row_number]) - 1:
                    result = []
                    if row_number != 0:
                        result.append(mat[row_number - 1][column_number])  # top neighbor
                    if column_number != len(mat[row_number]) - 1:
                        result.append(mat[row_number][column_number + 1])  # right neighbor
                    if row_number != len(mat) - 1:
                        result.append(mat[row_number + 1][column_number])  # bottom neighbor
                    if column_number != 0:
                        result.append(mat[row_number][column_number - 1])  # left neighbor

                else:
                    result = [
                        mat[row_number - 1][column_number],  # top neighbor
                        mat[row_number][column_number + 1],  # right neighbor
                        mat[row_number + 1][column_number],  # bottom neighbor
                        mat[row_number][column_number - 1]  # left neighbor
                    ]

    return print(result)



indexes1 = (1, 1)
N = 5
M = 7
mat = [[j + i * N for j in range(N)] for i in range(M)]
get_neighbourhood('moore',mat,indexes1)




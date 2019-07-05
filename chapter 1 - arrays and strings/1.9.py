def zero_matrix(matrix):
    empty_mat = []
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                empty_mat.append([i, j])

    for pos in empty_mat:
        for i in range(cols):
            matrix[pos[0]][i] = 0
        for j in range(rows):
            matrix[j][pos[1]] = 0
    print(matrix)


if __name__ == "__main__":
    matrix = [[1, 2, 3], [0, 2, 4], [9, 2, 1], [1, 1, 1]]
    mat1 = [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [2, 3, 4, 5, 6],
    ]
    # zero_matrix(matrix)
    zero_matrix(mat1)


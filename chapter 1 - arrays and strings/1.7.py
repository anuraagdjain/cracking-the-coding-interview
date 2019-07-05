def rotate_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    if rows != cols:
        print("not a square matrix")
        return
    result = [[0 for x in range(rows)] for y in range(cols)]
    for r in range(rows):
        for c in range(cols):
            result[c][rows - r - 1] = matrix[r][c]
    print(result)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 6], [4, 5, 6, 7], [7, 8, 9, 1], [11, 12, 13, 14]]
    rotate_matrix(matrix)

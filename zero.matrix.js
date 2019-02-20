'use strict';
const matrix = [[1, 2, 3], [0, 2, 4], [9, 2, 1], [1, 1, 1]];
const emptyPos = [];
const columns = matrix.length,
  rows = matrix[0].length;
for (let i = 0; i < rows; i++) {
  for (let j = 0; j < columns; j++) {
    if (matrix[i][j] === 0) {
      emptyPos.push([i, j]);
    }
  }
}

emptyPos.forEach(pos => {
  for (let i = 0; i < rows; i++) {
    matrix[pos[0]][i] = 0;
  }

  for (let i = 0; i < columns; i++) {
    matrix[i][pos[1]] = 0;
  }
});

console.log(matrix);

// output
// [[0, 2, 3], [0, 0, 0], [0, 2, 1], [0, 1, 1]]

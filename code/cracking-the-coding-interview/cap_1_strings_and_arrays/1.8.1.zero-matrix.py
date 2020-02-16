def zero_matrix(matrix):
  m = len(matrix)
  n = len(matrix[0])

  arr_rows = []
  arr_columns = []

  for i in range(m):
    for j in range(n):
      if matrix[i][j] == 0:
        if i not in arr_rows:
          arr_rows.append(i)

        if j not in arr_columns:
          arr_columns.append(j)
 
  for row in arr_rows:
    for i in range(n):
      matrix[row][i] = 0

  for column in arr_columns:
    for j in range(m):
      matrix[j][column] = 0

  return matrix

m = [
  [1, 2, 0],
  [2, 3, 3],
  [1, 2, 3],
  [0, 1, 1]
]

print(zero_matrix(m))
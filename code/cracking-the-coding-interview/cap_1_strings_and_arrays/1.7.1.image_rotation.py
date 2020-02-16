def rotate_image(matrix):
  n = len(matrix)
  if n <= 1:
    return matrix

  layers = int(n / 2)
  for layer in range(layers):
    offset_begin = layer
    offset_end = n - 1 - layer

    for i in range(offset_begin, offset_end):
      # creating a temp var to store top value
      temp = matrix[offset_begin][i]
      # rotating left to top
      matrix[offset_begin][i] = matrix[offset_end - i][offset_begin]
      # rotating bottom to left
      matrix[offset_end - i][offset_begin] = matrix[offset_end][offset_end - i]
      # rotating right to bottom
      matrix[offset_end][offset_end - i] = matrix[i][offset_end]
      # rotating top to right
      matrix[i][offset_end] = temp
      print(matrix)

  return matrix


m = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

m2 = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

'''
  Given a matrix NxN,
    Time efficiency: O(N^2)
    Memory efficiency: O(1)
'''
def rotateMatrix(matrix):
  n = len(matrix)
  if n == 0:
    return False

  layers = n / 2

  for layer in xrange(layers):
    offset_begin = layer
    offset_end = n - 1 - layer

    for i in xrange(offset_begin, offset_end):
      # temp variable to store top
      temp = matrix[offset_begin][i]

      # rotating left to top
      matrix[offset_begin][i] = matrix[offset_end - i][offset_begin]

      # rotating bottom to left
      matrix[offset_end - i][offset_begin] = matrix[offset_end][offset_end - i]

      # rotating right to bottom
      matrix[offset_end][offset_end - i] = matrix[i][offset_end]

      # rotating top to right
      matrix[i][offset_end] = temp   

  return matrix

matrix_4x4 =  [ 
  [1, 2, 3, 4], 
  [5, 6, 7, 8], 
  [9, 10, 11, 12],
  [13, 14, 15, 16]
]

matrix_3x3 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

rotated_matrix_4x4 = [
  [13, 9, 5, 1], 
  [14, 10, 6, 2], 
  [15, 7, 11, 3], 
  [16, 12, 8, 4]
]

rotated_matrix_3x3 = [
  [7, 4, 1], 
  [8, 5, 2], 
  [9, 6, 3]
]

def tests():
  assert rotateMatrix(matrix_3x3) == rotated_matrix_3x3
  assert rotateMatrix(matrix_4x4) == rotated_matrix_4x4
  assert rotateMatrix([[]]) == False

if __name__ == "__main__":
  tests()
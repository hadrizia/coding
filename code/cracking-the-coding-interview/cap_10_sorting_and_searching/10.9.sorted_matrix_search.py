'''
Input : 
  mat = [
    [1, 5, 9],
    [14, 20, 21],
    [30, 34, 43]
    ]
  x = 14
Output : (1, 0)

Input : 
  mat = [
    [1, 5, 9, 11],
    [14, 20, 21, 26],
    [30, 34, 43, 50]
    ]
  x = 42
Output : -1
'''

def search(matrix, x):
  if not matrix:
    return

  row = 0
  col = len(matrix[0]) - 1
  while row < len(matrix) and col >= 0:
    if matrix[row][col] == x:
      return (row, col)

    elif matrix[row][col] > x:
      col -= 1

    else:
      row += 1
  return -1

def tests():

  mat = [
      [1, 5, 9],
      [14, 20, 21],
      [30, 34, 43]
      ]

  assert search(mat, 14) == (1, 0)

  mat2 = [
      [1, 5, 9, 11],
      [14, 20, 21, 26],
      [30, 34, 43, 50]
      ]
  
  assert search(mat2, 42) == -1

tests()
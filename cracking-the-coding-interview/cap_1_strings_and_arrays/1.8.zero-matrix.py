def checkIfFirstRowHasZero(matrix):
  for i in xrange(len(matrix[0])):
    if matrix[0][i] == 0:
      return True
  return False

def checkIfFirstColumnHasZero(matrix):
  for i in xrange(len(matrix)):
    if matrix[i][0] == 0:
      return True
  return False

def fillColumnWithZero(matrix, index):
  for i in xrange(1, len(matrix[0])):
    matrix[i][index] = 0
  return matrix

def fillRowWithZero(matrix, index):
  for i in xrange(1, len(matrix)):
    matrix[index][i] = 0
  return matrix

'''
  Given that N = len(rows) and M = len(columns),
    Time efficiency: O(N*M)

'''
def zeroMatrix(matrix):
  n = len(matrix)
  m = len(matrix[0])

  first_row_has_zero = checkIfFirstRowHasZero(matrix)
  first_column_has_zero = checkIfFirstColumnHasZero(matrix)

  for i in xrange(1, n):
    for j in xrange(1, m):
      if matrix[i][j] == 0:
        matrix[i][0] = 0
        matrix[0][j] = 0

  for i in xrange(1, n):
    if matrix[i][0] == 0:
      matrix = fillRowWithZero(matrix, i)
    
    if matrix[0][i] == 0:
      matrix = fillColumnWithZero(matrix, i)
        
  return matrix

def tests():
  matrix = [
    [1, 1, 2],
    [3, 0, 5],
    [6, 7, 8]
  ]
  
  expected_matrix = [
    [1, 0, 2],
    [0, 0, 0],
    [6, 0, 8]
  ]
  assert zeroMatrix(matrix) == expected_matrix
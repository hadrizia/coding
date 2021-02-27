'''
  Input
  Several instances are given. The first line of the input contains n > 0, the number of matrices in the input. The following lines describe n matrices. Each matrix is described by 9 lines. These lines contain 9 integers each.

  Output
  For each instance, your program must print a line containing "Instancia k" , where k is the instance number. In the second line, your program must print "SIM" (portuguese for yes) if the given matrix is a solution to the puzzle, or "NAO" (portuguese for no) otherwise. Print an empty line after each instance.

  Link: https://www.urionlinejudge.com.br/judge/en/problems/view/1383
'''

from collections import defaultdict

def check_matrix(m, begin_x, end_x, begin_y, end_y):
  d = defaultdict(int)
  for i in range(begin_x, end_x + 1):
    for j in range(begin_y, end_y + 1):
      d[m[i][j]] += 1
      if d[m[i][j]] > 1:
        return False
  return True


def sudoku_aux():

  m = []
  for _ in range(9):
    row = [int(x) for x in input().split(" ")]

    # Check rows
    if len(row) != len(set(row)):
      return False

    m.append(row)
  
  # Check columns
  for i in range(9):
    columns = defaultdict(int)
    for j in range(9):
      columns[m[j][i]] += 1
      if columns[m[j][i]] > 1:
        return False
  
  # Check submatrixes
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      res = check_matrix(m, i, i + 2, j, j + 2)
      if not res:
        return False
  return True

def sudoku():
  execution_time = int(input())
  res = []
  for i in range(execution_time):
    res.append(sudoku_aux())
  for i in range(execution_time):
    res_print = 'SIM' if res[i] else 'NAO'
    print("Instancia", i + 1)
    print(res_print)
    print('')


sudoku()
NEG_INF = -64

def build_accum_sum(arr):
  acum_sum = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
  for j in xrange(len(arr)):
    acum_sum[0][j] = arr[0][j] + acum_sum[0][j - 1]
    acum_sum[j][0] = arr[j][0] + acum_sum[j - 1][0]

  for i in xrange(1, len(arr)):
    for j in xrange(1, len(arr[i])):
      acum_sum[i][j] = (arr[i][j] + acum_sum[i - 1][j] + acum_sum[i][j-1]) - acum_sum[i-1][j-1]
  return acum_sum

def find_sum(accum_sum, start_row, end_row, start_col, end_col):
  end_sum = accum_sum[end_row][end_col]
  left_square_sum = accum_sum[end_row][start_col - 1] if start_col else 0
  upper_square_sum = accum_sum[start_row - 1][end_col] if start_row else 0
  left_upper_square_sum = accum_sum[start_row - 1][start_col - 1] if (start_col and start_row) else 0
  return end_sum - left_square_sum - upper_square_sum + left_upper_square_sum


def getHourglassSum(arr, accum_sum, start_row, start_col):
  if start_row + 2 >= len(arr) or start_col + 2 >= len(arr[0]):
    return NEG_INF
  
  end_row = start_row + 2
  end_col = start_col + 2

  all_sum = find_sum(accum_sum, start_row, end_row, start_col, end_col)
  final_sum = all_sum - arr[start_row + 1][end_col] - arr[start_row + 1][start_col]
  return final_sum

def hourglassSum(arr):
  accum_sum = build_accum_sum(arr)
  max_hour_glass_sum = NEG_INF
  for row in range(len(arr)):
    for col in range(len(arr[0])):
      hour_glass_sum = getHourglassSum(arr, accum_sum, row, col)
      if hour_glass_sum > max_hour_glass_sum:
        max_hour_glass_sum = hour_glass_sum
  return max_hour_glass_sum

a = [[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]

b = [[1, 1, 1],
[0, 1, 2],
[1, 1, 2]]

print hourglassSum(a)
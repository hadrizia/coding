def findMax(arr, i):
  len_arr = len(arr)
  val_a = arr[i] if i >= 0 and i < len_arr else float('-inf')
  val_b = arr[i - 1] if i > 0 and i < len_arr else float('-inf')
  val_c = arr[i + 1] if i >= 0 and i < len_arr - 1 else float('-inf')

  max_value = max(val_a, val_b, val_c)
  if max_value == val_a:
    return i
  elif max_value == val_b:
    return i - 1
  return i + 1

def peaks_and_valleys(arr):
  for i in range(0, len(arr), 2):
    big = findMax(arr, i)
    if i != big:
      arr[i], arr[big] = arr[big], arr[i]
  return arr

assert peaks_and_valleys([5, 3, 1, 2, 3]) == [5, 1, 3, 2, 3]
assert peaks_and_valleys([1, 2, 1, 1, 0, 3, 2]) == [2, 1, 1, 1, 3, 0, 2]
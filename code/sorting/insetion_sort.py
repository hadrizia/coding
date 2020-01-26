def insertion_sort(array):
  for j in range(1, len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i -= 1
    array[i + 1] = key
  return(array)

def nonincreasing_insertion_sort(arr):
  for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] < key:
      arr[i + 1] = arr[i]
      i -= 1
    arr[i + 1] = key
  return arr

print insertion_sort([5, 2, 4, 6, 1, 3])
print nonincreasing_insertion_sort([5, 2, 4, 6, 1, 3])
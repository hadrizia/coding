def swap(arr, i, j):
  aux = arr[i]
  arr[i] = arr[j]
  arr[j] = aux

def countSwaps(arr):
  swaps = 0
  for i in xrange(len(arr)):
    for j in xrange(len(arr) - 1):
      if (arr[j] > arr[j + 1]):
            swap(arr, j, j + 1)
            swaps += 1
  print 'Array is sorted in %d swaps.' % swaps
  print 'First Element: %d' % arr[0]
  print 'Last Element: %d' % arr[-1]

arr = [1, 2, 3]

countSwaps(arr)

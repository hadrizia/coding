'''
  Time complexity: O(N/2 * logN) where N = len(arr)
  Space complexity: O(1)
'''

def sparse_search(arr, x):
  return search(arr, x, 0, len(arr) - 1)

def search(arr, x, l, r):
  if l > r:
    return
  
  m = (l + r) // 2

  if not arr[m]: # Search for the closest non empty str
    begin = m - 1
    end = m + 1

    while begin >= l and end <= r:
      if arr[begin]:
        m = begin
        break
      elif arr[end]:
        m = end
        break
      else:
        begin += 1
        end += 1

  if arr[m] == x:
    return m  
  
  if arr[m] > x: # Check the left side
      return search(arr, x, l, m - 1)
  else: # Check the right side
      return search(arr, x, m + 1, r)

def tests():
  arr = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
  assert sparse_search(arr, "ball") == 4
  assert sparse_search(arr, "dad") == 10